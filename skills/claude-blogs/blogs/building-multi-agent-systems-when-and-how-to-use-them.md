# Building Multi-Agent Systems: When and How to Use Them

**Source:** https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them  
**Published:** January 23, 2026  
**Categories:** Agents, Claude Platform

## Overview

A multi-agent system uses multiple LLM instances with separate contexts, coordinated through code. Teams have invested substantial effort building complex multi-agent systems only to discover that "improved prompting on a single agent achieved equivalent results." Multi-agent approaches typically consume 3-10x more tokens than single-agent solutions.

## When to Use Multi-Agent Systems

### 1. Context Protection
When an agent accumulates irrelevant information from subtasks, context pollution degrades performance. Specialized subagents isolate information in clean contexts.

### 2. Parallelization
Running multiple agents simultaneously enables exploration of larger search spaces. Valuable for research tasks investigating different facets independently, then synthesizing results.

### 3. Specialization
Different tasks benefit from tailored tool sets, system prompts, or domain expertise. Rather than overwhelming one agent with dozens of tools, specialized agents with focused responsibilities improve reliability.

**Tool set specialization**: Helps when agents manage 20+ tools or domains overlap confusingly.
**System prompt specialization**: Addresses conflicting behavioral requirements.
**Domain expertise specialization**: Allows agents to carry focused knowledge.

## Context-Centric Decomposition

**Problem-centric (counterproductive)**: Separating work by role creates constant handoff overhead and loses context at each transfer.

**Context-centric (effective)**: Dividing by context boundaries means agents handling related work share necessary understanding. "Work should only be split when context can be truly isolated."

## The Verification Subagent Pattern

A dedicated agent validates the main agent's work. Requires concrete criteria like "Run the full test suite and report all failures" rather than vague directives.

## Key Signals for Multi-Agent Readiness

Consider multi-agent architectures when:
- Approaching context limits with degrading performance
- Managing 15-20+ tools
- Tasks naturally decompose into independent, parallelizable pieces

"Start with the simplest approach that works, and add complexity only when evidence supports it."
