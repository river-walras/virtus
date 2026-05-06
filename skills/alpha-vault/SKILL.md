---
name: alpha-vault
description: Build or refresh a portable strategy knowledge base for this repository by bundling notebooks, local markdown notes, and code implementations into a skill-local `ref/` folder. Use when Codex needs to answer research questions about these strategies, locate implementation files, refresh the repository's reference corpus, or search topic summaries from a self-contained skill bundle.
---

# Alpha Vault

Keep the knowledge base inside this skill. Prefer bundled notebook content and bundled code context over raw PDF extraction or external repo-relative references.

## Workflow

1. Rebuild the skill-local references:

```bash
python3 skills/alpha-vault/scripts/build_ref.py
```

2. Read the generated overview first:
   - `skills/alpha-vault/ref/index.md`
3. Open the topic ref that matches the user's question.
4. Use the bundled `source/` files listed in that topic ref. They are copied into the skill so the bundle still works after separate installation.
5. Search with `rg`:

```bash
rg -n "RSRS|动量|波动率" skills/alpha-vault/ref
rg -n "NoiseArea|FScore" skills/alpha-vault/ref
```

## Reference Policy

- Prefer bundled notebook content as the main conceptual summary and the main ripgrep surface.
- Bundle local `.md` notes and `README.md` files when they exist.
- Bundle `.py` implementation files when they exist.
- Do not rely on external repo-relative PDF pointers inside generated refs.
- Re-run the builder after adding notebooks, docs, or code.
