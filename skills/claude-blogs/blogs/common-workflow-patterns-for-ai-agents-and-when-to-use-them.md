# Common workflow patterns for AI agents—and when to use them

**Source:** https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them  
**Published:** March 5, 2026  
**Categories:** Agents, Claude Platform

## Overview

AI agents operate within workflows that establish execution patterns for complex problems requiring coordinated steps. Three patterns dominate production use cases: sequential, parallel, and evaluator-optimizer workflows.

## Understanding Workflows vs. Autonomous Agents

Workflows establish boundaries for how agents apply reasoning and tool use. A fully autonomous agent decides everything about task execution, while a workflow provides structural guardrails that allow dynamic behavior within defined paths.

## The Three Core Workflow Patterns

### Sequential Workflows

Execute tasks in predetermined order, where each stage processes inputs and passes results to the next step.

**Best for:** Multi-stage processes with clear dependencies, data transformation pipelines, draft-review-polish cycles.

**Trade-offs:** Adds latency since each step waits for the previous one, but can improve accuracy.

**Examples:** Content generation followed by translation; document extraction → validation → database loading.

### Parallel Workflows

Distribute independent tasks across multiple agents executing simultaneously, then merge results.

**Best for:** Evaluation across multiple dimensions, code review processes, document analysis.

**Trade-offs:** Increases API costs due to concurrent calls; requires clear aggregation strategies.

**Examples:** Quality metric evaluation where each agent assesses different dimensions; code review examining different vulnerability categories.

### Evaluator-Optimizer Workflows

Pair generation and evaluation agents in iterative cycles: the generator produces content while the evaluator assesses against specific criteria.

**Best for:** Code generation with specific requirements, professional communications, technical documentation.

**Trade-offs:** Multiplies token usage and adds iteration time, but produces higher-quality outputs.

**Examples:** API documentation with completeness verification; SQL query generation checked for efficiency.

## Selection Guidance

Start with the simplest approach. Try a single agent first. If that meets quality standards, implementation is complete.

- Sequential: when tasks have dependencies
- Parallel: when independent subtasks benefit from simultaneous processing
- Evaluator-optimizer: only when iterative refinement demonstrably improves quality

These patterns aren't mutually exclusive—nest them as complexity requires.
