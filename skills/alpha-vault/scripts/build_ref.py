#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
REF_DIR = SKILL_DIR / "ref"
TOP_LEVELS = ("A-量化基本面", "B-因子构建类", "C-择时类", "D-组合优化")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a portable report-kb ref bundle from notebooks, markdown docs, and code."
    )
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="Repository root.")
    parser.add_argument("--ref-dir", type=Path, default=REF_DIR, help="Skill ref output dir.")
    return parser.parse_args()


def slugify(text: str) -> str:
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"[^\w\-\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "item"


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def stable_name(path: Path) -> str:
    digest = hashlib.sha1(path.as_posix().encode("utf-8")).hexdigest()[:8]
    return f"{slugify(path.stem)}-{digest}{path.suffix}"


def sanitize_markdown(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\(data:image/[^)]+\)", "_[embedded image omitted]_", text)
    text = re.sub(r"<img[^>]+src=['\"]data:image/[^>]+>", "_[embedded image omitted]_", text)
    return text.strip()


def topic_dirs(root: Path) -> list[Path]:
    result: list[Path] = []
    for top_name in TOP_LEVELS:
        top_dir = root / top_name
        if not top_dir.exists():
            continue
        result.extend(sorted(p for p in top_dir.iterdir() if p.is_dir()))
    return result


def read_notebook_intro(path: Path) -> str:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return ""

    blocks: list[str] = []
    for cell in data.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        text = sanitize_markdown("".join(cell.get("source", [])))
        if not text:
            continue
        blocks.append(text)
        if len("\n\n".join(blocks)) >= 2500 or len(blocks) >= 3:
            break
    return "\n\n".join(blocks).strip()


def doc_excerpt(path: Path, max_chars: int = 1800) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

    lines = [line.rstrip() for line in text.splitlines()]
    cleaned: list[str] = []
    for line in lines:
        if not line.strip():
            cleaned.append("")
            continue
        cleaned.append(line)
        if len("\n".join(cleaned)) >= max_chars:
            break
    return sanitize_markdown("\n".join(cleaned).strip())


def list_notebooks(topic_dir: Path) -> list[Path]:
    return sorted(
        p for p in topic_dir.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts
    )


def list_docs(topic_dir: Path) -> list[Path]:
    return sorted(set(topic_dir.rglob("*.md")))


def list_code_files(topic_dir: Path) -> list[Path]:
    return sorted(p for p in topic_dir.rglob("*.py") if p.is_file())


def extract_symbols(py_path: Path) -> list[str]:
    try:
        text = py_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = py_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []

    symbols: list[str] = []
    for line in text.splitlines():
        match = re.match(r"\s*(?:def|class)\s+([A-Za-z_][A-Za-z0-9_]*)", line)
        if match:
            symbols.append(match.group(1))
        if len(symbols) >= 12:
            break
    return symbols


def choose_primary_notebook(notebooks: list[Path]) -> Path | None:
    ranked: list[tuple[int, int, str, Path]] = []
    for path in notebooks:
        intro = read_notebook_intro(path)
        ranked.append((0 if intro else 1, len(path.parts), path.as_posix(), path))
    return sorted(ranked)[0][3] if ranked else None


def copy_source_files(files: list[Path], dest_dir: Path) -> list[dict[str, str]]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, str]] = []
    for src in files:
        dest_name = stable_name(src)
        dest = dest_dir / dest_name
        shutil.copy2(src, dest)
        copied.append(
            {
                "source_path": src.as_posix(),
                "dest_name": dest_name,
                "suffix": src.suffix,
            }
        )
    return copied


def render_topic_ref(
    topic_dir: Path,
    bundle_dir: Path,
    notebooks: list[dict[str, str]],
    docs: list[dict[str, str]],
    code_files: list[dict[str, str]],
) -> str:
    primary_nb_path = choose_primary_notebook([Path(item["source_path"]) for item in notebooks])
    primary_nb = None
    if primary_nb_path:
        primary_nb = next(
            (item for item in notebooks if item["source_path"] == primary_nb_path.as_posix()),
            None,
        )
    primary_intro = read_notebook_intro(primary_nb_path) if primary_nb_path else ""

    lines = [
        f"# {topic_dir.name}",
        "",
        f"- Category: `{topic_dir.parent.name}`",
        f"- Bundle Dir: `{bundle_dir.name}`",
        "",
    ]

    if primary_nb:
        lines.extend(
            [
                "## Primary Summary",
                "",
                f"- Notebook: `source/{primary_nb['dest_name']}`",
                "",
                primary_intro or "_No markdown introduction found in the primary notebook._",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Primary Summary",
                "",
                "_No notebook found. Use bundled docs and code below._",
                "",
            ]
        )

    if notebooks:
        lines.extend(["## Notebooks", ""])
        for nb in notebooks:
            intro = read_notebook_intro(Path(nb["source_path"]))
            lines.append(f"### `source/{nb['dest_name']}`")
            lines.append("")
            lines.append(intro or "_No markdown introduction found._")
            lines.append("")

    if docs:
        lines.extend(["## Local Docs", ""])
        for doc in docs:
            excerpt = doc_excerpt(Path(doc["source_path"]))
            lines.append(f"### `source/{doc['dest_name']}`")
            lines.append("")
            lines.append(excerpt or "_Unable to read markdown excerpt._")
            lines.append("")

    if code_files:
        lines.extend(["## Code Implementation", ""])
        for code_path in code_files:
            lines.append(f"- `source/{code_path['dest_name']}`")
            symbols = extract_symbols(Path(code_path["source_path"]))
            if symbols:
                lines.append(f"  - Symbols: `{', '.join(symbols)}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_index(entries: list[dict[str, str]]) -> str:
    lines = [
        "# Alpha Vault Ref Index",
        "",
        f"- Total topics: **{len(entries)}**",
        "- Priority order: bundled ipynb -> bundled local markdown docs -> bundled code implementation",
        "",
        "| Category | Topic | Ref | Bundle |",
        "| --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['category']}` | `{entry['topic']}` | `{entry['ref_path']}` | `{entry['bundle_dir']}` |"
        )
    lines.append("")
    return "\n".join(lines)


def clear_old_refs(ref_dir: Path) -> None:
    for path in ref_dir.rglob("*"):
        if path.is_file():
            path.unlink()
    for path in sorted((p for p in ref_dir.rglob("*") if p.is_dir()), reverse=True):
        if path != ref_dir:
            path.rmdir()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    ref_dir = args.ref_dir.resolve()
    ref_dir.mkdir(parents=True, exist_ok=True)
    clear_old_refs(ref_dir)
    ref_dir.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, str]] = []

    for topic_dir in topic_dirs(root):
        category_dir = ref_dir / slugify(topic_dir.parent.name)
        bundle_dir = category_dir / slugify(topic_dir.name)
        source_dir = bundle_dir / "source"
        bundle_dir.mkdir(parents=True, exist_ok=True)

        notebook_paths = list_notebooks(topic_dir)
        doc_paths = list_docs(topic_dir)
        code_paths = list_code_files(topic_dir)

        copied_notebooks = copy_source_files(notebook_paths, source_dir)
        copied_docs = copy_source_files(doc_paths, source_dir)
        copied_code = copy_source_files(code_paths, source_dir)

        summary_path = bundle_dir / "summary.md"
        summary_path.write_text(
            render_topic_ref(topic_dir, bundle_dir, copied_notebooks, copied_docs, copied_code),
            encoding="utf-8",
        )

        entries.append(
            {
                "category": topic_dir.parent.name,
                "topic": topic_dir.name,
                "ref_path": rel(summary_path, root),
                "bundle_dir": rel(bundle_dir, root),
            }
        )

    index_path = ref_dir / "index.md"
    index_path.write_text(render_index(entries), encoding="utf-8")
    (ref_dir / "index.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "topic_count": len(entries),
                "ref_dir": rel(ref_dir, root),
                "index": rel(index_path, root),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
