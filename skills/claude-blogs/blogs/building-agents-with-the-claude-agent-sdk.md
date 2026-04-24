# Building agents with the Claude Agent SDK

**Source:** https://claude.com/blog/building-agents-with-the-claude-agent-sdk  
**Published:** September 29, 2025  
**Categories:** Claude Code, Agents

## Overview

Anthropic renamed the Claude Code SDK to the **Claude Agent SDK**, reflecting its broader application. The SDK enables developers to create autonomous agents by providing computer-like capabilities—file management, command execution, and iterative improvement.

## Key Design Principle

Agents need the same tools programmers use daily: find files in a codebase, write and edit files, lint code, run it, debug, edit—iteratively.

## Agent Types You Can Build

- Finance agents (portfolio analysis, investment evaluation)
- Personal assistants (calendars, travel, briefings)
- Customer support agents (complex service tickets)
- Research agents (comprehensive document analysis)

## The Agent Loop Framework

**Gather context → Take action → Verify work → Repeat**

### Gathering Context

- **Agentic search/file systems**: Use bash (`grep`, `tail`) to retrieve relevant information; folder structure as context engineering
- **Semantic search**: Faster but less accurate and harder to maintain—start with agentic approaches
- **Subagents**: Enable parallelization and context isolation; multiple agents work simultaneously, returning only pertinent information
- **Compaction**: SDK automatically summarizes previous messages as context limits approach

### Taking Action

- **Tools**: Custom tools are primary agent actions—design efficiently to maximize context usage
- **Bash and scripts**: General-purpose command execution (convert PDFs, download attachments)
- **Code generation**: Excels at precise, reusable code for documents, spreadsheets, presentations
- **MCPs**: Standardized integrations to Slack, GitHub, Asana without custom OAuth

### Verifying Work

- **Rules-based feedback**: Defined output rules with specific failure explanations; code linting provides detailed feedback
- **Visual feedback**: Screenshots and renders verify UI layout, spacing, styling
- **LLM as judge**: Separate model evaluates fuzzy criteria (with latency tradeoffs)

## Testing and Improvement

Examine failures carefully:
- Does the agent have access to necessary information through proper search APIs?
- Can formal rules in tool calls prevent repeated failures?
- Do agents need additional creative tools?
- Should representative test sets be built for programmatic evaluation?
