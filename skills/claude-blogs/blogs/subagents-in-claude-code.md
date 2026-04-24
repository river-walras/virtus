# How and when to use subagents in Claude Code

**Source:** https://claude.com/blog/subagents-in-claude-code  
**Published:** April 7, 2026  
**Categories:** Claude Code, Coding

## Overview

Claude Code subagents are isolated instances with independent context windows that handle specific tasks without burdening the main conversation. They enable parallel processing, research delegation, and unbiased reviews.

## What is a Subagent?

Subagents operate as self-contained assistants that work independently to explore codebases, read files, or make changes. Each starts fresh without conversation history, can run in parallel with others, and returns only relevant results.

Types: general-purpose agents, plan agents (research-first), and explore agents (read-only code searching).

## When to Use Subagents

- **Research-heavy tasks**: Delegate exploration work before implementation
- **Multiple independent tasks**: Parallel subagents complete non-dependent work simultaneously
- **Fresh perspective needed**: Unbiased review from an agent lacking conversation history
- **Verification before committing**: Independent verification catches blind spots
- **Pipeline workflows**: Sequential phases (design → implement → test)

**Key indicator:** Tasks requiring 10+ files or 3+ independent pieces signal subagent appropriateness.

## How to Direct Subagents

**Conversational Invocation**: Natural language across all Claude Code interfaces. Example: "Use subagents to explore authentication, database schema, and API endpoints simultaneously."

**Custom Subagents**: Reusable specialists live in `.claude/agents/` (project-level) or `~/.claude/agents/` (user-level). Each has its own system prompt, tool permissions, and optional model selection.

**CLAUDE.md Instructions**: Define policies for when Claude should delegate.

**Skills**: Complex multi-step workflows in `.claude/skills/` as reusable interfaces.

**Hooks**: User-defined commands executing automatically at lifecycle points.

## When NOT to Use Subagents

- Sequential dependent work where step two needs step one's full output
- Same-file parallel edits (conflict risk)
- Small, quick tasks where delegation overhead exceeds benefit
- Excessive specialist agents (reliability decreases with roster size)
- Work requiring subagent-to-subagent coordination (use agent teams instead)
