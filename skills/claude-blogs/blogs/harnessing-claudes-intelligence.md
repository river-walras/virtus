# Harnessing Claude's Intelligence

**Source:** https://claude.com/blog/harnessing-claudes-intelligence  
**Published:** April 2, 2026  
**Categories:** Agents, Claude Platform

## Building applications that balance intelligence, latency, and cost

## 1. Use what Claude knows

Build applications using tools Claude understands well. In late 2024, Claude 3.5 Sonnet achieved 49% on SWE-bench Verified using only a bash tool and text editor tool. Claude Code uses these same tools.

Claude composes these general tools into various patterns solving different problems—including Agent Skills, programmatic tool calling, and memory functionality.

## 2. Ask "what can I stop doing?"

Agent frameworks encode assumptions about Claude's abilities. As Claude becomes more capable, those assumptions require testing.

### Let Claude orchestrate its own actions

A common assumption: every tool result must flow through Claude's context window. Providing Claude with a code execution tool lets it write code expressing tool calls and logic between them, determining what to pass through, filter, or pipe forward without expanding the context window.

On BrowseComp, giving Opus 4.6 the ability to filter tool outputs improved accuracy from 45.3% to 61.6%.

### Let Claude manage its own context

Providing Claude access to skills addresses context scaling. Each skill's YAML frontmatter offers a brief description in the context window, with full content disclosed progressively when Claude calls the read file tool.

Context editing selectively removes stale or irrelevant information. With Opus 4.6, subagent spawning improved BrowseComp results by 2.8% over single-agent approaches.

### Let Claude persist its own context

Compaction lets Claude summarize past context to maintain continuity on extended tasks. On BrowseComp search tasks, Sonnet 4.5 stayed flat at 43% regardless of compaction budget, yet Opus 4.5 scaled to 68% and Opus 4.6 reached 84%.

A memory folder enables Claude to write context to files and read them later. On BrowseComp-Plus, giving Sonnet 4.5 a memory folder increased accuracy from 60.4% to 67.2%.

## 3. Set boundaries carefully

### Design context to maximize cache hits

Key principles:
- **Static first, dynamic last**: Order requests so stable content (system prompt, tools) comes first
- **Messages for updates**: Append a `<system-reminder>` in messages rather than editing prompts
- **Don't change models**: Caches are model-specific
- **Carefully manage tools**: Adding or removing a tool invalidates the cache

### Use declarative tools for UX, observability, or security boundaries

Dedicated tools offer action-specific hooks that frameworks can intercept, gate, render, or audit. Reversibility serves as a useful criterion; hard-to-reverse actions like external API calls warrant user confirmation.
