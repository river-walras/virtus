# Seeing like an agent: how we design tools in Claude Code

**Source:** https://claude.com/blog/seeing-like-an-agent  
**Published:** April 10, 2026  
**Categories:** Claude Code, Coding

## Understanding Agent-Centered Tool Design

Building effective AI agents requires more than just adding features—it demands understanding how the model thinks. Anthropic's Claude Code team approaches tool design by adopting the agent's perspective, asking what capabilities would best serve Claude's own problem-solving abilities.

The core principle: "give it tools that are shaped to its own abilities." Rather than choosing between one general-purpose tool or fifty specialized ones, designers must match tools to the model's actual strengths and limitations.

## The AskUserQuestion Tool: Three Iterations

When building better elicitation capabilities, the team tried multiple approaches:

**Initial attempt:** Adding a questions parameter to the ExitPlanTool proved confusing, mixing plan generation with question asking in ways that muddled Claude's reasoning.

**Second approach:** Requesting Claude output questions in a custom markdown format failed consistently. The model would "append extra sentences, drop options, or abandon the structure altogether."

**Final solution:** A dedicated AskUserQuestion tool that Claude could call at any point, displaying results in a modal and blocking execution until users responded. This worked because it gave Claude "a structured output" while ensuring multiple options appeared reliably.

## Progressive Evolution with Capability Growth

As models improve, previously helpful tools can become constraints. Claude Code initially used a TodoWrite tool with system reminders every five turns. However, stronger models like Opus 4.5 found these reminders limiting—they encouraged sticking to original plans rather than adapting when circumstances changed.

The solution was replacing todos with a more flexible Task tool supporting dependencies and cross-agent coordination, demonstrating that "the tools that your models once needed might now be constraining them."

## Context Discovery Through Search

Rather than pre-indexing codebases with RAG, Claude Code evolved toward giving Claude search capabilities. This shift—from being "given context" to "finding context itself"—proved more adaptable across different environments.

The introduction of Agent Skills formalized "progressive disclosure," allowing models to "incrementally discover relevant context through exploration." Skills files could reference other files recursively, enabling nested searches for precise information.

## Progressive Disclosure in Practice

With roughly 20 tools, the team maintains a high bar for additions since each option increases the model's decision complexity. When users asked about Claude Code features, rather than bloating the system prompt, developers created a subagent that searches documentation independently and returns only relevant answers.

This approach—"adding things to Claude's action space without adding a new tool"—demonstrates how good design can expand capabilities through structure rather than proliferation.

## The Core Insight

Tool design remains more art than science, varying by model, goals, and environment. Success requires continuous experimentation and close attention to model behavior: "Try to see like an agent."
