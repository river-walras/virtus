# Mode checklists

One section per mode. Each lists must-haves, recommended visual patterns, and an example prompt drawn from Thariq's article.

---

## `spec` — Specs, planning, exploration

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

**Example prompt:**
> "I'm not sure what direction to take the onboarding screen. Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's making."

---

## `code-review` — PR walkthroughs and code understanding

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
- Highlight.js or similar for syntax coloring (CDN OK).

**Example prompt:**
> "Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity and whatever else might be needed to convey the concept well."

---

## `design` — Designs and prototypes

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

**Example prompt:**
> "I want to prototype a new checkout button — when clicked it does a play animation and then turns purple quickly. Create an HTML file with several sliders and options for me to try different options on this animation, give me a copy button to copy the parameters that worked well."

---

## `report` — Reports, research, learning

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
- Dark-mode friendly (`prefers-color-scheme`).

**Example prompt:**
> "I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a 'gotchas' section at the bottom. Optimize it for someone reading it once."

---

## `editor` — Custom throwaway editing interfaces

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

**Example prompts:**
> "I need to reprioritize these 30 Linear tickets. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns. Pre-sort them by your best guess. Add a 'copy as markdown' button that exports the final ordering with a one-line rationale per bucket."

> "Here's our feature flag config. Build a form-based editor for it — group flags by area, show dependencies between them, warn me if I enable a flag whose prerequisite is off. Add a 'copy diff' button that gives me just the changed keys."

> "I'm tuning this system prompt. Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, three sample inputs on the right that re-render the filled template live. Add a character/token counter and a copy button."
