# Building agents with Skills: Equipping agents for specialized work

**Source:** https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work  
**Published:** January 22, 2026  
**Categories:** Agents, Claude Code

## Overview

Skills package domain expertise in files that agents can access and apply, transforming general-purpose AI systems into knowledgeable specialists for real-world tasks.

## What Are Agent Skills?

Skills organize collections of files containing domain expertise, workflows, best practices, and scripts. Files are versioned with Git, stored in cloud services, and shared across teams.

A typical skill:
- SKILL.md (metadata and documentation)
- Supporting files (scripts, templates, guides)
- References directory (additional documentation on demand)

## Progressive Disclosure Architecture

Three-tier approach:
- **Metadata tier** (~50 tokens): Name and description visible at all times
- **Full documentation** (~500 tokens): Complete SKILL.md loaded when needed
- **Reference materials** (2,000+ tokens): Supporting files accessed only upon request

## Skills as Tools

Rather than relying on traditional tool implementations, skills embed executable scripts. Scripts are self-documenting, modifiable by the model, and don't require continuous context allocation.

## Emerging Skill Categories

**Foundational skills**: Universal capabilities for document manipulation and spreadsheet work.
**Partner skills**: From companies like Notion and Browserbase, integrating their services directly.
**Enterprise skills**: Capturing internal processes and compliance requirements.

## Vertical-Specific Deployments

**Financial Services**: DCF modeling, comparable company analysis, earnings processing, research report generation.

**Healthcare & Life Sciences**: Genomic pipeline management, clinical trial protocol development, health data interoperability, prior authorization workflows.

## Complete Agent Architecture

1. Agent loop — Core reasoning system
2. Agent runtime — Execution environment
3. MCP servers — External tool connections
4. Skills library — Domain expertise
