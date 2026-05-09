# Design defaults

Baseline visual identity when no `design_reference` is provided. Aim: clean, modern, readable, dark-mode-friendly. Not flashy — the content is the point.

## Palette

Use CSS custom properties. Light theme by default, dark via `prefers-color-scheme: dark`.

```css
:root {
  --bg: #fafaf9;
  --surface: #ffffff;
  --border: #e7e5e4;
  --text: #1c1917;
  --text-muted: #57534e;
  --accent: #2563eb;
  --accent-soft: #dbeafe;
  --success: #15803d;
  --warning: #b45309;
  --danger: #b91c1c;
  --code-bg: #f5f5f4;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0c0a09;
    --surface: #1c1917;
    --border: #292524;
    --text: #f5f5f4;
    --text-muted: #a8a29e;
    --accent: #60a5fa;
    --accent-soft: #1e3a8a;
    --success: #4ade80;
    --warning: #fbbf24;
    --danger: #f87171;
    --code-bg: #1c1917;
  }
}
```

## Typography

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: var(--text);
  background: var(--bg);
}
code, pre {
  font-family: "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  font-size: 0.92em;
}
h1 { font-size: 2rem; line-height: 1.2; letter-spacing: -0.02em; }
h2 { font-size: 1.5rem; line-height: 1.25; letter-spacing: -0.01em; }
h3 { font-size: 1.15rem; }
```

## Layout

- Prose content: `max-width: 720px; margin: 0 auto; padding: 2rem 1.25rem;`
- Wider content (grids, dashboards, editors): `max-width: 1200px;`
- Generous vertical rhythm: `h2 { margin-top: 2.5rem; } p { margin: 0.75rem 0; }`
- Mobile: drop padding to `1rem`, single-column grids below 640px.

## Components

**Code blocks:**
```css
pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.875rem 1rem;
  overflow-x: auto;
}
```

**Callouts:**
```css
.callout {
  border-left: 3px solid var(--accent);
  background: var(--accent-soft);
  padding: 0.75rem 1rem;
  border-radius: 0 6px 6px 0;
  margin: 1rem 0;
}
```

**Tables:**
- Full width, alternating row tint via `tbody tr:nth-child(even)`.
- Border-bottom on header, no vertical borders.
- Padding `0.6rem 0.75rem` per cell.

**Buttons (for interactive artifacts):**
```css
button {
  font: inherit;
  background: var(--accent);
  color: white;
  border: 0;
  border-radius: 6px;
  padding: 0.5rem 0.9rem;
  cursor: pointer;
}
button:hover { filter: brightness(1.05); }
button.secondary { background: var(--surface); color: var(--text); border: 1px solid var(--border); }
```

## Recommended CDN libs (only when justified)

- **Highlight.js** — syntax highlighting for `code-review` and `report`.
- **Mermaid** — flowcharts when SVG-by-hand would be too much work.
- **D3** — only for genuinely data-bound visualizations.

If you include any of these, the document must still be readable when the CDN fails (graceful degradation).
