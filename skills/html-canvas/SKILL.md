---
name: html-canvas
description: Generate a rich, self-contained HTML artifact for specs, code reviews, designs, reports, or custom editors. Use when the user asks for an "HTML file/artifact/explainer/report/playground", wants a shareable visual deliverable instead of markdown, or asks to "make a canvas/dashboard/diagram-heavy doc". Trigger phrases include "make an HTML", "html artifact", "html canvas", "html report", "html explainer", "html playground", "visual spec", "html mockup".
---

# html-canvas

Produce a single, self-contained HTML artifact tailored to one of five archetype use-cases. Inspired by Thariq's "Unreasonable Effectiveness of HTML" — HTML is denser, more readable, more shareable, and supports two-way interaction in a way markdown cannot.

## When to use

| Mode | Use when the user wants… |
|---|---|
| `spec` | Brainstorming, comparing approaches, or an implementation plan with mockups. |
| `code-review` | A PR walkthrough, annotated diff, or focused review of a code area. |
| `design` | Visual designs, component prototypes, animation tuning, or design-system artifacts. |
| `report` | An explainer, research summary, status report, or technical deep-dive. |
| `editor` | A throwaway purpose-built UI to triage/edit/tune data, ending with an export. |

If the user asks for something HTML-shaped that doesn't clearly map to one of these, ask which mode fits or pick the closest and tell them.

## Parameters

**Required:**
- `mode` — one of `spec` | `code-review` | `design` | `report` | `editor`.
- `topic` — what the artifact is about (free text).
- `output_path` — absolute path to write the HTML file. Default `./<slug>.html` if omitted.

**Optional:**
- `sources` — list of files, directories, URLs, or MCP queries to ingest as context. For `code-review`, also pull `git diff` / `git log` automatically.
- `design_reference` — path to an existing HTML file whose visual style should be matched.
- `interactive` — boolean. When true, include knobs/sliders/forms plus a "Copy as prompt/JSON/markdown" export button so changes flow back to Claude Code. Defaults to true for `design` and `editor`, false otherwise.
- `open_after` — boolean. When true, run `open <path>` after writing.

## Workflow

1. **Resolve mode.** If missing or ambiguous, ask the user before doing anything else.
2. **Ingest sources.** Read files, fetch URLs (WebFetch), run MCP queries as specified. For `code-review`, also gather `git diff` and recent `git log`.
3. **Load design.** If `design_reference` is given, read it and extract palette, typography, spacing, component styles. Otherwise use `references/design-defaults.md`.
4. **Load mode checklist.** Read `references/modes.md` for the chosen mode and follow its must-haves and visual patterns.
5. **Generate.** Write a single self-contained HTML file to `output_path`. Inline all CSS and JS; no build step. CDN libs (D3, Mermaid, Highlight.js) are allowed when they meaningfully improve the result, but the file must still degrade gracefully offline.
6. **Open.** If `open_after`, run `open <output_path>`.

## Constraints

- **Single file.** Inline CSS and JS. No bundlers. No external local assets.
- **Offline-friendly.** If you use a CDN lib, the document's primary content must still be readable without it.
- **Mobile-responsive.** Use sensible breakpoints; avoid fixed widths.
- **Interactive exports.** Whenever the artifact accepts user input, include a button that copies the resulting state as prompt/JSON/markdown so the user can paste it back into Claude Code.
- **Don't pad.** Match length to content. A 200-line report is fine; a 2000-line report nobody reads is not.
- **Taste over templates.** Don't ship boilerplate sections that aren't earned by the content.

## References

- `references/modes.md` — per-mode must-haves, visual patterns, example prompts.
- `references/design-defaults.md` — baseline palette, typography, and component styles when no `design_reference` is provided.
