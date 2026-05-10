# Mode checklists

One section per mode. Each lists must-haves, recommended visual patterns, canonical example files (read at least one before generating), and an example prompt drawn from Thariq's article.

All examples live in `references/examples/`. Read them with the Read tool — they are the ground truth for the visual style.

## Interaction level defaults

`interaction_level=auto` maps to these defaults:

| Mode | Default | Expected behavior |
|---|---|---|
| `spec` | `light` | Comparison toggles, tabs/accordions, jump links, and copy buttons for the chosen direction or implementation prompt when useful. |
| `code-review` | `light` | Severity/file filters, collapsible diffs, anchor links, and a copyable review summary or reviewer prompt. |
| `design` | `full` | Live controls for tunable parameters, previews that update in place, and copy/export of selected parameters. |
| `report` | `light` | Table of contents, detail toggles, source links, and copy buttons for TL;DR, key findings, or follow-up prompt when useful. |
| `editor` | `full` | Direct manipulation, validation, reset/undo where cheap, and a prominent Copy as X export. |

Use `none` only when interaction would distract from a short static artifact. Use `full` outside `design`/`editor` when the user needs to tune, triage, simulate, annotate, or export state.

---

## `spec` — Specs, planning, exploration

**Canonical examples to read before generating:**
- `references/examples/01-exploration-code-approaches.html` — 3-col approach comparison
- `references/examples/02-exploration-visual-designs.html` — visual variant grid
- `references/examples/16-implementation-plan.html` — full implementation plan layout

**Purpose:** Help the user think through a problem with a rich canvas: option comparisons, mockups, data-flow diagrams, code snippets, and an implementation plan.

**Must-haves:**
- A clear problem statement at the top.
- At least one of: option-comparison grid, mockup section, data-flow diagram, annotated code snippet.
- An implementation plan section with concrete steps and file paths if code is involved.
- Tradeoff labels on each option ("favors X over Y").

**Visual patterns:**
- Side-by-side grid for comparing N approaches (CSS grid, equal columns).
- SVG arrows/boxes for data flow.
- Tabbed or accordion navigation when the doc gets long.
- Mockups rendered as actual HTML/CSS, not images.
- `interaction_level=auto`: include light controls such as tabs, compare filters, jump links, or a copyable selected recommendation when they help the decision.

**Example prompt:**
> "I'm not sure what direction to take the onboarding screen. Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's making."

---

## `code-review` — PR walkthroughs and code understanding

**Canonical examples to read before generating:**
- `references/examples/03-code-review-pr.html` — full PR review with risk map
- `references/examples/04-code-understanding.html` — explainer for unfamiliar code
- `references/examples/17-pr-writeup.html` — PR description companion

**Purpose:** Make a diff or code area legible to a reviewer who doesn't have the same context as the author.

**Must-haves:**
- The actual diff rendered (not paraphrased), with line numbers.
- Margin annotations explaining non-obvious changes.
- Severity color-coding for findings (info / nit / concern / blocker).
- A "focus area" callout if the user named one.
- A short summary of what the PR does and why.

**Visual patterns:**
- Side-by-side or unified diff with sticky file headers.
- Color bar in the left margin per finding severity.
- Collapsible sections per file.
- Severity/file filters plus a copyable review summary when findings span multiple files.
- Highlight.js or similar for syntax coloring (CDN OK).

**Example prompt:**
> "Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity and whatever else might be needed to convey the concept well."

---

## `design` — Designs and prototypes

**Canonical examples to read before generating:**
- `references/examples/05-design-system.html` — token swatches, type scale, spacing ruler
- `references/examples/06-component-variants.html` — side-by-side component variants
- `references/examples/07-prototype-animation.html` — animation tuning with sliders
- `references/examples/08-prototype-interaction.html` — interaction prototype

**Purpose:** Sketch visual designs, prototype interactions, or tune component parameters live.

**Must-haves:**
- The component/screen rendered as actual interactive HTML.
- Sliders/knobs for any tunable parameter (timing, color, size, easing).
- A "Copy parameters" button that exports the current values as JSON or CSS.
- For multi-variant explorations: a side-by-side grid of variants.

**Visual patterns:**
- Control panel pinned to the side or top.
- Live preview that updates on input.
- Real CSS animations and transitions, not GIF mockups.
- Parameter values visible next to their controls.
- `interaction_level=auto`: use full interaction with sliders, toggles, editable values, and a copy/export button for the chosen parameters.

**Example prompt:**
> "I want to prototype a new checkout button — when clicked it does a play animation and then turns purple quickly. Create an HTML file with several sliders and options for me to try different options on this animation, give me a copy button to copy the parameters that worked well."

---

## `report` — Reports, research, learning

**Canonical examples to read before generating:**
- `references/examples/09-slide-deck.html` — scroll-snap fullscreen slides
- `references/examples/10-svg-illustrations.html` — inline SVG diagram patterns
- `references/examples/11-status-report.html` — status / weekly report layout
- `references/examples/12-incident-report.html` — incident postmortem
- `references/examples/13-flowchart-diagram.html` — flowchart-heavy explainer
- `references/examples/14-research-feature-explainer.html` — feature deep-dive with sticky sidebar
- `references/examples/15-research-concept-explainer.html` — concept explainer with tabbed code samples

**Purpose:** Synthesize information from multiple sources into something readable in one sitting.

**Must-haves:**
- A 1–3 sentence TL;DR at the top.
- SVG diagrams for any flow, architecture, or sequence that matters.
- 3–5 annotated code snippets if the report covers code.
- A "gotchas" or "things that surprised me" section near the end.
- Links/citations back to the underlying sources where possible.

**Visual patterns:**
- Single-column readable width (~720px max for prose).
- SVG flowcharts inline, not as separate images.
- Pull quotes and callouts for emphasis.
- Optional table of contents for longer reports.
- Optional `.invert` sections for intentional dark slides or emphasis blocks; do not use automatic `prefers-color-scheme` unless the user asks for system dark mode.
- `interaction_level=auto`: include light navigation, expandable details, source links, and copy buttons for TL;DR or follow-up prompts when useful.

**Example prompt:**
> "I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a 'gotchas' section at the bottom. Optimize it for someone reading it once."

---

## `editor` — Custom throwaway editing interfaces

**Canonical examples to read before generating:**
- `references/examples/18-editor-triage-board.html` — kanban triage with drag + copy-as-markdown
- `references/examples/19-editor-feature-flags.html` — form-based config editor with dependency warnings
- `references/examples/20-editor-prompt-tuner.html` — side-by-side prompt editor with live preview

**Purpose:** A purpose-built UI for one specific piece of data the user wants to manipulate. Not a product — a tool for this one task.

**Must-haves:**
- The data loaded in and rendered as the right primitive (cards, form, table, canvas).
- Direct manipulation appropriate to the data (drag, edit-in-place, toggle).
- A prominent **Copy as X** button (JSON, markdown, prompt, diff — whatever fits).
- Validation/warnings for constraints the user mentioned.

**Visual patterns:**
- Whatever fits the data: kanban for triage, form for config, side-by-side for prompt tuning.
- Minimal chrome — the data is the UI.
- Show counts/stats live (token count, item count, changed-keys count).
- Undo or reset where it costs little to add.
- `interaction_level=auto`: use full interaction with direct manipulation, validation, live counts, and a prominent export.

**Example prompts:**
> "I need to reprioritize these 30 Linear tickets. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns. Pre-sort them by your best guess. Add a 'copy as markdown' button that exports the final ordering with a one-line rationale per bucket."

> "Here's our feature flag config. Build a form-based editor for it — group flags by area, show dependencies between them, warn me if I enable a flag whose prerequisite is off. Add a 'copy diff' button that gives me just the changed keys."

> "I'm tuning this system prompt. Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, three sample inputs on the right that re-render the filled template live. Add a character/token counter and a copy button."
