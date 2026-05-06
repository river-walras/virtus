#!/usr/bin/env python3
"""Fetch new claude.com/blog posts and update this skill.

The script intentionally avoids LLM summarization. It extracts structured text
from official Claude blog pages and writes source-grounded markdown files that
future agents can inspect and summarize as needed.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import textwrap
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


BLOG_ROOT = "https://claude.com/blog"
AUTO_START = "<!-- AUTO-GENERATED: recent-posts START -->"
AUTO_END = "<!-- AUTO-GENERATED: recent-posts END -->"


@dataclass
class BlogPost:
    url: str
    slug: str
    title: str
    published: str
    categories: list[str]
    description: str
    content: list[str]


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip_depth += 1
        if tag in {"h1", "h2", "h3", "p", "li", "div", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        if tag in {"h1", "h2", "h3", "p", "li", "div"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        value = data.strip()
        if value:
            self.parts.append(value + " ")

    def text(self) -> str:
        value = "".join(self.parts)
        value = html.unescape(value)
        value = value.replace("\u200d", "")
        value = re.sub(r"[ \t]+", " ", value)
        value = re.sub(r"\n\s*\n+", "\n", value)
        return value.strip()


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "claude-blogs-skill-updater/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def extract_listing_urls(html_text: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for match in re.finditer(r'href=["\'](?:https://claude\.com)?/blog/([^"\'?#]+)', html_text):
        slug = match.group(1).strip("/")
        if not slug or "/" in slug:
            continue
        url = f"{BLOG_ROOT}/{slug}"
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def clean_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def value_after(lines: list[str], label: str) -> str:
    for index, line in enumerate(lines):
        if line == label and index + 1 < len(lines):
            return lines[index + 1]
    return ""


def values_between(lines: list[str], start: str, stops: Iterable[str]) -> list[str]:
    stop_set = set(stops)
    for index, line in enumerate(lines):
        if line == start:
            values: list[str] = []
            for value in lines[index + 1 :]:
                if value in stop_set:
                    break
                if value not in values:
                    values.append(value)
            return values
    return []


def extract_description(html_text: str) -> str:
    patterns = [
        r'<meta\s+content="([^"]+)"\s+name="description"',
        r'<meta\s+name="description"\s+content="([^"]+)"',
        r'<meta\s+property="og:description"\s+content="([^"]+)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, html_text, flags=re.I)
        if match:
            return html.unescape(match.group(1)).strip()
    return ""


def parse_post(url: str, html_text: str) -> BlogPost:
    parser = TextExtractor()
    parser.feed(html_text)
    lines = clean_lines(parser.text())
    slug = url.rstrip("/").split("/")[-1]

    title = ""
    breadcrumb_index = -1
    for index, line in enumerate(lines):
        if line == "/" and index + 1 < len(lines):
            title = lines[index + 1]
            breadcrumb_index = index + 1
            break
    if not title:
        title = slug.replace("-", " ").title()

    description = extract_description(html_text)
    if not description and breadcrumb_index >= 0:
        for line in lines[breadcrumb_index + 1 :]:
            if line in {"Explore here", "Category", "Product", "Date"}:
                continue
            if line not in {title, "Ask questions about this page", "Copy as markdown"}:
                description = line
                break

    published = value_after(lines, "Date")
    categories = values_between(lines, "Category", {"Product", "Date", "Reading time", "Share"})
    categories = [item for item in categories if item != "No items found."]

    content_start = -1
    for index, line in enumerate(lines):
        if line == url:
            content_start = index + 1
            break
    if content_start < 0 and breadcrumb_index >= 0:
        content_start = breadcrumb_index + 1

    stop_markers = {
        "No items found.",
        "Prev Prev",
        "Related posts",
        "Transform how your organization operates with Claude",
        "Get the developer newsletter",
        "FAQ",
    }
    body: list[str] = []
    for line in lines[content_start:]:
        if line in stop_markers:
            break
        if line in {
            title,
            "Explore here",
            "Ask questions about this page",
            "Copy as markdown",
            "Category",
            "Product",
            "Date",
            "Reading time",
            "Share",
            "Copy link",
            "min",
        }:
            continue
        if line == url or line in categories or line == published:
            continue
        body.append(line)

    return BlogPost(
        url=url,
        slug=slug,
        title=title,
        published=published or "Unknown",
        categories=categories or ["Uncategorized"],
        description=description,
        content=body,
    )


def wrap_paragraph(text: str) -> str:
    if re.match(r"^[-*] ", text) or re.match(r"^\d+\. ", text):
        return text
    return "\n".join(textwrap.wrap(text, width=100, break_long_words=False, break_on_hyphens=False))


def post_to_markdown(post: BlogPost) -> str:
    lines = [
        f"# {post.title}",
        "",
        f"**Source:** {post.url}  ",
        f"**Published:** {post.published}  ",
        f"**Categories:** {', '.join(post.categories)}",
        "",
    ]
    if post.description:
        lines.extend(["## Overview", "", wrap_paragraph(post.description), ""])
    lines.extend(["## Extracted Content", ""])
    if post.content:
        for paragraph in post.content:
            lines.append(wrap_paragraph(paragraph))
            lines.append("")
    else:
        lines.extend(["No body content could be extracted from the page.", ""])
    lines.extend(
        [
            "## When to Use This Blog",
            "",
            "Use this source when a question matches the title, categories, or extracted content above.",
            "",
        ]
    )
    return "\n".join(lines)


def read_urls(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def write_urls(path: Path, new_urls: list[str], existing_urls: list[str]) -> None:
    ordered: list[str] = []
    seen: set[str] = set()
    for url in [*new_urls, *existing_urls]:
        if url not in seen:
            seen.add(url)
            ordered.append(url)
    path.write_text("\n".join(ordered) + "\n")


def extract_metadata(markdown: str, url: str, slug: str) -> BlogPost:
    title_match = re.search(r"^#\s+(.+)$", markdown, flags=re.M)
    published_match = re.search(r"^\*\*Published:\*\*\s+(.+?)\s*$", markdown, flags=re.M)
    categories_match = re.search(r"^\*\*Categories:\*\*\s+(.+?)\s*$", markdown, flags=re.M)
    overview_match = re.search(r"^## Overview\s+(.+?)(?:\n## |\Z)", markdown, flags=re.M | re.S)
    description = ""
    if overview_match:
        description = " ".join(clean_lines(overview_match.group(1)))[:220]
    return BlogPost(
        url=url,
        slug=slug,
        title=title_match.group(1).strip() if title_match else slug.replace("-", " ").title(),
        published=published_match.group(1).strip() if published_match else "Unknown",
        categories=[
            item.strip()
            for item in (categories_match.group(1) if categories_match else "Uncategorized").split(",")
            if item.strip()
        ],
        description=description,
        content=[],
    )


def update_counts(skill_path: Path, index_path: Path, count: int) -> None:
    for path in [skill_path, index_path]:
        if not path.exists():
            continue
        text = path.read_text()
        text = re.sub(r"\b\d+\s+official claude\.com/blog posts", f"{count} official claude.com/blog posts", text)
        text = re.sub(r"all\s+\d+\s+blog posts", f"all {count} blog posts", text, flags=re.I)
        text = re.sub(r"organizes\s+\d+\s+blogs", f"organizes {count} blogs", text)
        path.write_text(text)


def index_row(post: BlogPost) -> str:
    question = post.description or f"Source for {post.title}."
    question = re.sub(r"\s+", " ", question).strip()
    if len(question) > 150:
        question = question[:147].rstrip() + "..."
    return f"| `{post.slug}.md` | {post.published} | {', '.join(post.categories)} | {question} |"


def sort_key(post: BlogPost) -> tuple[datetime, str]:
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            return (datetime.strptime(post.published, fmt), post.title)
        except ValueError:
            pass
    return (datetime.min, post.title)


def update_recent_index(index_path: Path, posts: list[BlogPost]) -> None:
    if not index_path.exists():
        return
    posts = sorted(posts, key=sort_key, reverse=True)
    rows = "\n".join(index_row(post) for post in posts)
    block = "\n".join(
        [
            "## Recently Fetched Posts",
            "",
            AUTO_START,
            "| File | Published | Categories | What it answers |",
            "|------|-----------|------------|-----------------|",
            rows,
            AUTO_END,
            "",
            "---",
        ]
    )
    text = index_path.read_text()
    if AUTO_START in text and AUTO_END in text:
        pattern = re.compile(
            r"## Recently Fetched Posts\n\n"
            + re.escape(AUTO_START)
            + r".*?"
            + re.escape(AUTO_END)
            + r"\n\n---",
            flags=re.S,
        )
        text = pattern.sub(block, text)
    else:
        marker = "---"
        text = text.replace(marker, block, 1)
    index_path.write_text(text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--force", action="store_true", help="regenerate markdown for listed posts")
    parser.add_argument("--dry-run", action="store_true", help="show changes without writing files")
    args = parser.parse_args()

    root = args.root
    blogs_dir = root / "blogs"
    urls_path = root / "urls.txt"
    index_path = root / "index.md"
    skill_path = root / "SKILL.md"

    listing_html = fetch(BLOG_ROOT)
    live_urls = extract_listing_urls(listing_html)
    if not live_urls:
        print("No blog URLs found on listing page.", file=sys.stderr)
        return 1

    existing_urls = read_urls(urls_path)
    existing_set = set(existing_urls)
    new_urls = [url for url in live_urls if url not in existing_set]

    posts_for_recent_index: list[BlogPost] = []
    created: list[Path] = []
    updated: list[Path] = []

    for url in live_urls:
        slug = url.rstrip("/").split("/")[-1]
        output_path = blogs_dir / f"{slug}.md"
        if output_path.exists() and not args.force:
            posts_for_recent_index.append(extract_metadata(output_path.read_text(), url, slug))
            continue

        post = parse_post(url, fetch(url))
        posts_for_recent_index.append(post)
        if args.dry_run:
            continue
        blogs_dir.mkdir(parents=True, exist_ok=True)
        output_path.write_text(post_to_markdown(post))
        if url in existing_set:
            updated.append(output_path)
        else:
            created.append(output_path)

    new_urls_ordered = [
        post.url
        for post in sorted(
            [post for post in posts_for_recent_index if post.url in set(new_urls)],
            key=sort_key,
            reverse=True,
        )
    ]
    final_urls = [*new_urls_ordered, *existing_urls]
    final_count = len(set(final_urls))
    if not args.dry_run:
        write_urls(urls_path, new_urls_ordered, existing_urls)
        update_counts(skill_path, index_path, final_count)
        update_recent_index(index_path, posts_for_recent_index)

    print(f"Live listing URLs: {len(live_urls)}")
    print(f"New URLs: {len(new_urls)}")
    print(f"Total tracked URLs: {final_count}")
    if args.dry_run:
        for url in new_urls:
            print(f"Would fetch: {url}")
    else:
        for path in created:
            print(f"Created: {path.relative_to(root)}")
        for path in updated:
            print(f"Updated: {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
