# pdf-resume-skills

A Claude Code skill that builds a distinctive, production-grade personal website from a resume PDF.

## What it does

The `resume-website` skill guides you through building a custom personal website tailored to your profession and design preferences. It:

1. Extracts content from your resume PDF
2. Analyzes your profession to determine an appropriate aesthetic direction
3. Asks about your design preferences (vibe, colors, typography, animations)
4. Generates a fully static HTML/CSS/JS website — no build tools, no frameworks

## Installation

This skill depends on the `frontend-design` skill for generating polished UI. Install both:

```bash
npx skills add https://github.com/anthropics/skills --skill frontend-design
npx skills add river-walras/pdf-resume-skills
```

## Usage

Drop your resume PDF into your project directory, then invoke the skill:

```
/resume-website
```

Claude will walk you through the process interactively.

## PDF Extraction

The skill uses a `uv`-powered Python script to extract text from the PDF. Make sure [`uv`](https://github.com/astral-sh/uv) is installed:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

You can also run the extraction script directly:

```bash
uv run scripts/pdf-extract.py path/to/resume.pdf
```

## Output

The skill produces a static website in your current directory:

- `index.html` — main page
- `assets/` — images and media (if provided)
- `style.css` — styles (if extracted from inline)

Open `index.html` in any browser to view the result.
