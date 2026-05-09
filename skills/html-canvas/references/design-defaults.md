# Default style: warm editorial earth-tone

This is the canonical visual identity for `html-canvas` outputs, extracted from Thariq's "Unreasonable Effectiveness of HTML" examples in `references/examples/`. Use this unless `design_reference` overrides it.

## Aesthetic

Soft minimal brutalism. Clean lines, generous whitespace, warm earth-tone palette (clay, olive, slate, oat, ivory). Serif display headings paired with system sans body create an editorial, paper-like feel. Subtle depth via 1.5px borders and small soft shadows on hover — never glassmorphic, never neumorphic, never gradient-heavy. Frame-perfect transitions at 120ms. The content is the design; ornament is restrained.

## CSS custom properties

Drop this into `:root` of every artifact.

```css
:root {
  /* Earth-tone palette */
  --clay: #D97757;        /* primary action, emphasis */
  --clay-d: #B85C3E;      /* clay hover */
  --olive: #788C5D;       /* success, positive */
  --slate: #141413;       /* text, strong elements */
  --oat: #E3DACC;         /* secondary backgrounds, highlights */
  --ivory: #FAF9F5;       /* page background */
  --white: #FFFFFF;       /* card surfaces */
  --rust: #B04A3F;        /* danger, deletion */
  --warning: #C78E3F;     /* amber */
  --info: #5C7CA3;        /* muted blue */

  /* Warm grays */
  --gray-100: #F0EEE6;
  --gray-300: #D1CFC5;
  --gray-500: #87867F;
  --gray-700: #3D3D3A;

  /* Spacing — 8px base */
  --sp-1: 4px;  --sp-2: 8px;  --sp-3: 12px; --sp-4: 16px;
  --sp-5: 24px; --sp-6: 32px; --sp-7: 48px; --sp-8: 64px;

  /* Radius */
  --r-pill: 999px;
  --r-card: 14px;
  --r-panel: 12px;
  --r-row: 8px;
  --r-icon: 5px;

  /* Fonts */
  --font-serif: ui-serif, Georgia, "Times New Roman", serif;
  --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Monaco, Consolas, monospace;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--ivory);
  color: var(--slate);
  font: 400 15px/1.55 var(--font-sans);
  padding: 56px 32px 96px;
}
```

## Typography

| Use | Family | Size | Weight | Line-height |
|---|---|---|---|---|
| Display | serif | `clamp(40px, 6vw, 64px)` | 500 | 1.1 |
| H1 | serif | `clamp(32px, 4vw, 40px)` | 500 | 1.2 |
| H2 | serif | 21–27px | 500 | 1.3 |
| Body | sans | 15–16px | 400 | 1.55–1.6 |
| Small | sans | 14px | 430 | 1.5 |
| **Eyebrow / label** | mono | 11–12px UPPERCASE, `letter-spacing: 0.08em–0.12em`, `color: var(--gray-500)` | 500 | 1.4 |
| Code (block) | mono | 12.5px on slate bg, off-white `#E8E6DE` text | 400 | 1.65 |
| Code (inline) | mono | 13px, `padding: 1px 6px`, `background: var(--gray-100)`, `border-radius: 4px` | — | — |

Syntax tokens: `.kw{color:var(--clay)} .str{color:var(--olive)} .cm{color:var(--gray-500)} .fn{color:#C9B98A}`.

## Layout

- **Page wrap**: `max-width: 980–1120px; margin: 0 auto;` — pick 980 for prose, 1120 for grids.
- **Reading column**: `max-width: 700px` on `<p>` blocks inside wider pages.
- **Sidebar layout**: `display:grid; grid-template-columns: 200px minmax(0,1fr); gap: 48px;` Sticky sidebar `top: 32px`.
- **Card grids**: `grid-template-columns: repeat(auto-fill, minmax(316px, 1fr)); gap: 24px;`
- **Section rhythm**: `h2 { margin-top: 48–72px; }`, paragraphs `0.75rem 0`.
- **Breakpoints**: 1100 (3-col → 1-col), 920 (drop sidebar), 640 (compact, single-column, padding 16px).

## Components

### Buttons

```css
.btn { height: 36px; padding: 0 16px; border-radius: var(--r-row); font: 500 14px/1 var(--font-sans);
       border: 1.5px solid transparent; cursor: pointer;
       transition: background .12s ease, border-color .12s ease, color .12s ease; }
.btn-primary { background: var(--clay); color: var(--white); }
.btn-primary:hover { background: var(--clay-d); }
.btn-secondary { background: var(--white); color: var(--slate); border-color: var(--gray-300); }
.btn-secondary:hover { background: var(--gray-100); }
.btn-ghost { background: transparent; color: var(--gray-700); }
.btn-ghost:hover { background: var(--gray-100); }
.btn-danger { background: var(--rust); color: var(--white); }
.btn-danger:hover { background: #9A3F3F; }
```

### Cards & panels

```css
.card { background: var(--white); border: 1.5px solid var(--gray-300);
        border-radius: var(--r-card); padding: 20px 24px;
        transition: border-color .15s ease, transform .15s ease, box-shadow .15s ease; }
.card:hover { transform: translateY(-3px); border-color: var(--slate);
              box-shadow: 0 10px 30px rgba(20,20,19,.10); }
```

### Code blocks (incl. diff)

```css
pre { background: var(--slate); color: #E8E6DE; padding: 18px 20px;
      border-radius: var(--r-panel); overflow-x: auto;
      font: 400 12.5px/1.65 var(--font-mono); }
.diff-row { display: grid; grid-template-columns: 48px 16px 1fr; gap: 8px; }
.diff-row.add { background: rgba(120,140,93,.15); }
.diff-row.del { background: rgba(176,74,63,.15); }
.diff-row .ln { color: var(--gray-500); text-align: right; user-select: none; }
```

### Callouts

```css
.callout { border-left: 3px solid var(--clay); background: rgba(217,119,87,.06);
           padding: 14px 18px; border-radius: 0 10px 10px 0; margin: 16px 0; }
.callout strong { color: var(--clay); font-weight: 600; }
```

### Badges / chips

```css
.badge { display: inline-flex; align-items: center; height: 22px; padding: 0 9px;
         border-radius: var(--r-pill); font: 500 12px/1 var(--font-mono); }
.badge-neutral { background: var(--gray-100); color: var(--gray-700); }
.badge-accent  { background: rgba(217,119,87,.14); color: var(--clay); }
.badge-success { background: rgba(120,140,93,.16); color: var(--olive); }
.badge-warn    { background: rgba(199,142,63,.18); color: var(--warning); }
.badge-danger  { background: rgba(176,74,63,.14); color: var(--rust); }
```

### Inputs

```css
input, select, textarea {
  height: 38px; padding: 0 12px; font: 400 14px/1.4 var(--font-sans);
  background: var(--white); color: var(--slate);
  border: 1.5px solid var(--gray-300); border-radius: var(--r-row);
}
input:focus { outline: none; border-color: var(--clay);
              box-shadow: 0 0 0 3px rgba(217,119,87,.15); }
input::placeholder { color: var(--gray-500); }
```

Custom checkbox: `appearance:none; width:18px; height:18px; border:1.5px solid var(--gray-300); border-radius:4px;` checked → `background:var(--clay); border-color:var(--clay);` with a ::after checkmark.

### SVG diagram class system

Inline SVGs use a small class vocabulary:

```css
.st { fill: none; stroke: var(--gray-500); stroke-width: 2.5; stroke-linecap: round; }
.lc { fill: none; stroke: var(--clay);     stroke-width: 2.5; stroke-linecap: round; }
.da { stroke-dasharray: 4 4; }
.fl { fill: var(--gray-300); }
.cl { fill: var(--clay); }
.ol { fill: var(--olive); }
.oa { fill: var(--oat); }
.sl { fill: var(--slate); }
.wh { fill: var(--white); }
```

## Mode-specific idioms (quick reference)

- **spec**: 3-column comparison grid, each card has title + description + code snippet + tradeoff list. End with a recommendation block (clay left border, serif h2).
- **code-review**: PR header (repo / author / branch / +/- stats) → risk map (chip buttons jumping to file anchors) → file cards with sticky headers + diff + comment `bubbles` (severity left-border colors) → checklist footer.
- **design**: `:root` tokens block displayed as swatches → typography table → spacing ruler → radius/shadow cards → live `.component-stage` showing buttons/inputs/badges in action.
- **report**: optional scroll-snap fullscreen slides (`scroll-snap-type: y mandatory`) with `.slide.invert` for slate-bg sections; SVG flowcharts; thin (5px) progress bars; large serif metric numbers with delta indicators.
- **editor**: sticky toolbar at top, then 4-col kanban (`repeat(4,1fr)` with sticky col-heads `top:0; z-index:1`) OR form-based layout. Drag with `.dragover` outline feedback. Always end with a "Copy as X" button that flashes olive + text "Copied ✓" for 1200ms.

## Interaction patterns

- **Transitions**: 120–180ms, `ease` / `ease-out`, never custom cubic-bezier. Properties: `border-color, background, color, box-shadow, transform, opacity`.
- **Hover**: `transform: translateY(-3px)` on cards; `background` shift on rows/buttons.
- **Copy-to-clipboard**: `navigator.clipboard.writeText(text)` with textarea fallback; UX = swap button text, add `.copied` class, `setTimeout(revert, 1200)`.
- **Tabs**: `data-t="N"` attributes on triggers and panels, toggle `.on` class.
- **Drag**: native HTML5 drag-and-drop, `.dragover` adds outline + tint.
- **Keyboard**: arrow keys for slide nav (`document.addEventListener('keydown', e => e.key === 'ArrowRight' && next())`).

## What NOT to do

- ❌ No frameworks (React, Vue, Svelte, Alpine).
- ❌ No utility CSS (Tailwind, UnoCSS). Use semantic class names.
- ❌ No custom web fonts. System stacks only.
- ❌ No gradients except a single hero figure when really justified.
- ❌ No build step. Single `.html` file with inline `<style>` and `<script>`.
- ❌ No JS animation libraries (GSAP, anime.js). Pure CSS transitions.
- ❌ No neumorphism, no glassmorphism (`backdrop-filter`), no heavy `filter: drop-shadow`.
- ❌ No `prefers-color-scheme` dark mode. Inversion is done with `.invert` on specific sections (slate bg + ivory text).
- ❌ No CSS resets beyond `* { box-sizing: border-box; }`.

## Worked example: minimal report skeleton

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Topic</title>
<style>
  :root { /* paste palette block above */ }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--ivory); color:var(--slate);
         font:400 15px/1.55 var(--font-sans); padding:56px 32px 96px; }
  .wrap { max-width: 980px; margin: 0 auto; }
  .eyebrow { font: 500 11px/1.4 var(--font-mono); text-transform: uppercase;
             letter-spacing: .12em; color: var(--gray-500); }
  h1 { font: 500 clamp(32px,4vw,40px)/1.2 var(--font-serif);
       margin: 8px 0 24px; letter-spacing: -.01em; }
  h2 { font: 500 24px/1.3 var(--font-serif); margin: 56px 0 16px; }
  .callout { border-left: 3px solid var(--clay); background: rgba(217,119,87,.06);
             padding: 14px 18px; border-radius: 0 10px 10px 0; margin: 16px 0; }
</style>
</head>
<body>
  <main class="wrap">
    <div class="eyebrow">Report · 2026-05-09</div>
    <h1>Topic title</h1>
    <div class="callout"><strong>TL;DR</strong> One- to three-sentence summary.</div>
    <h2>Section</h2>
    <p>Body content...</p>
  </main>
</body>
</html>
```
