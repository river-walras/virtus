# Improving skill-creator: Test, measure, and refine Agent Skills

**Source:** https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills  
**Published:** March 3, 2026  
**Categories:** Claude Code

## Overview

Anthropic has enhanced its skill-creator tool with new capabilities enabling authors to verify skills function correctly, identify quality regressions, and iteratively improve performance without requiring coding expertise.

## Key Improvements

### Testing Framework
Supports evaluation writing—automated tests checking whether Claude produces expected outputs for given prompts. Identifies when skills break with new models and signals when capability-enhancement skills may no longer be necessary.

### Benchmark Mode
Standardized assessment tool measuring skill performance by tracking evaluation pass rates, execution time, and token consumption. Results can be stored locally or integrated into dashboards and CI systems.

### Multi-Agent Evaluation
Independent agents run tests in parallel within isolated contexts, eliminating cross-contamination between test runs. Comparator agents enable A/B testing between skill versions.

### Description Optimization
Analyzes skill descriptions against sample prompts, suggesting refinements that reduce false-positive and false-negative triggering. Testing showed improvement in 5 of 6 public document-creation skills' triggering precision.

## Skill Categories

- **Capability uplift skills**: Enable Claude to perform tasks the base model cannot execute consistently
- **Encoded preference skills**: Sequence existing capabilities according to organizational workflows

## Availability

Available on Claude.ai, Cowork, and as a plugin for Claude Code users.
