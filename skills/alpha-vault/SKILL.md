---
name: alpha-vault
description: Portable strategy knowledge base for this repository — bundled notebooks, local markdown notes, and code implementations grouped by topic under the skill's own `ref/` folder. Use when answering research questions about these strategies, locating implementation files, or searching topic summaries from a self-contained skill bundle.
---

# Alpha Vault

A pre-built, self-contained corpus of quant strategy references. Each topic has its own folder with a `summary.md` (notebook content + notes) and a `source/` directory holding the original `.ipynb`, `.md`, and `.py` files bundled into the skill so it works after separate installation.

## Prerequisites

This skill searches with `rg` (ripgrep). If it's not installed, install it first:

```bash
command -v rg >/dev/null || brew install ripgrep   # macOS
command -v rg >/dev/null || sudo apt-get install -y ripgrep   # Debian/Ubuntu
```

## Workflow

1. Read the topic index to find what's relevant:
   - `ref/index.md` — human-readable table of all 55 topics by category
   - `ref/index.json` — same data, machine-readable

2. Open the matching topic's `summary.md` for the conceptual writeup.

3. For implementation details, read files under that topic's `source/` directory (notebooks, notes, and `.py` files are bundled there).

4. Search across the whole corpus with `rg`. Always scope to `ref/` to keep results focused:

   ```bash
   rg -n "RSRS|动量|波动率" ref/
   rg -n "NoiseArea|FScore" ref/
   rg --files-with-matches "因子择时" ref/        # just the topics that mention it
   rg -n -g '*.ipynb' "def compute" ref/          # search inside bundled notebooks
   ```

   Run from the skill directory so the relative `ref/` path resolves; otherwise pass the absolute path to the skill's `ref/` folder.

## Reference Policy

- Treat the bundled `summary.md` as the primary conceptual source and the main ripgrep surface.
- For code questions, go to the topic's `source/` files rather than re-deriving from the summary.
- The corpus is pre-built and shipped with the skill; no rebuild step is needed. Add new topics by dropping a folder under the appropriate category in `ref/` with a `summary.md` and a `source/` directory, then update `ref/index.md` and `ref/index.json`.
