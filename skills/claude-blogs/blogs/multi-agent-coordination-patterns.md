# Multi-agent coordination patterns: Five approaches and when to use them

**Source:** https://claude.com/blog/multi-agent-coordination-patterns  
**Published:** April 10, 2026  
**Categories:** Agents, Claude Platform, Coding

## Overview

When building multi-agent systems, teams often select patterns based on perceived sophistication rather than fit. The recommendation is to start with the simplest approach and evolve based on observed limitations. This article examines five distinct coordination patterns and their respective strengths and weaknesses.

## Pattern 1: Generator-Verifier

### How it works
A generator produces initial output that passes to a verifier for evaluation. The verifier either accepts the output or rejects it with feedback routed back to the generator for revision. This cycle continues until acceptance or maximum iterations are reached.

### Strengths
This simplest multi-agent pattern excels where output quality is critical and evaluation criteria can be explicitly defined. Examples: code generation with automated testing, fact-checking, compliance verification, rubric-based grading.

### Limitations
The verifier performs only as well as its criteria. Without explicit evaluation standards, verification becomes superficial. The pattern also assumes verification and generation represent separable skills. Iterative loops risk stalling if the generator cannot address feedback.

## Pattern 2: Orchestrator-Subagent

### How it works
A lead agent plans work and delegates tasks to specialized subagents, which complete their assignments and return results. The orchestrator synthesizes findings into final output.

### Strengths
Works well for clear task decomposition with minimal interdependence. Examples: automated code review systems where different agents handle security checks, test coverage analysis, code style assessment, and architectural evaluation.

### Limitations
The orchestrator becomes an information bottleneck. When one subagent's discovery affects another's work, information must route back through the orchestrator, often losing critical details through summarization.

## Pattern 3: Agent Teams

### How it works
A coordinator spawns multiple worker agents as independent processes that claim tasks from a shared queue and work autonomously across extended periods. Unlike orchestrator-subagent models, teammates persist and accumulate domain-specific context.

### Strengths
Suits parallel workloads benefiting from sustained, multi-step work. Example: codebase migration where each teammate migrates an independent service, developing familiarity with its specific dependencies and patterns.

### Limitations
Independence remains critical. Teammates operating autonomously cannot easily share intermediate findings, risking conflicting outputs.

## Pattern 4: Message Bus

### How it works
Agents interact through publish-subscribe primitives. Agents subscribe to topics of interest, and a router delivers matching messages.

### Strengths
Excels for event-driven pipelines where workflow emerges from events rather than predetermined sequences. Example: security operations where alerts flow through classification, investigation, enrichment, and response coordination stages.

### Limitations
Event-driven flexibility makes debugging difficult. Silent failures occur when routers misclassify or drop events.

## Pattern 5: Shared State

### How it works
Agents operate autonomously, reading from and writing directly to persistent storage without central coordination.

### Strengths
Removes the coordinator as a single point of failure. In research synthesis systems, multiple agents investigating different aspects can build on each other's discoveries immediately.

### Limitations
Without explicit coordination, agents may duplicate work or pursue contradictory approaches. Reactive loops pose problems requiring first-class termination conditions: time budgets, convergence thresholds, or designated agents evaluating when sufficient answers exist.

## Choosing Between Patterns

- **Orchestrator-subagent**: When subtasks are short, focused, and produce clear outputs
- **Agent teams**: When subtasks benefit from sustained, multi-step work building accumulated context
- **Message bus**: When workflow emerges from events and the agent ecosystem will grow
- **Shared state**: When agents build on each other's findings collaboratively

For most use cases, orchestrator-subagent provides the widest applicability. Observe specific failure points, then evolve toward other patterns as distinct needs become apparent.
