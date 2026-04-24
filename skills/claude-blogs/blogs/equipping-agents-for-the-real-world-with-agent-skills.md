# Equipping agents for the real world with Agent Skills

**Source:** https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills  
**Published:** October 16, 2025  
**Categories:** Claude Code, Agents

## Overview

Agent Skills is a framework for equipping AI agents with specialized capabilities through organized folders containing instructions, scripts, and resources—transforming general-purpose agents into specialized ones.

## What Are Agent Skills?

Skills package domain expertise into composable resources. Rather than building custom agents for each use case, developers specialize agents using reusable procedural knowledge. The concept mirrors creating an onboarding guide for new employees.

## Skill Architecture

A skill is a directory containing a `SKILL.md` file with YAML frontmatter specifying `name` and `description`. This enables **progressive disclosure**—Claude loads skill metadata initially, then reads full content only when relevant.

Complex skills can bundle additional files (like `reference.md` or `forms.md`) referenced from the main `SKILL.md`, allowing skills to grow substantially while keeping context window usage efficient.

## Code Execution Integration

Skills can include pre-written code scripts that Claude executes as tools—useful for deterministic operations where traditional code outperforms token generation (e.g., sorting lists, extracting PDF form fields).

## Development Guidelines

- **Start with evaluation**: Identify capability gaps through testing
- **Structure for scale**: Split unwieldy files, organize mutually exclusive contexts separately
- **Adopt Claude's perspective**: Monitor real-world usage and iterate
- **Collaborate iteratively**: Work with Claude to capture successful approaches into reusable context

## Security

Skills introduce potential vulnerabilities. Only install skills from trusted sources. Thoroughly audit skills before use, examining code dependencies, bundled resources, and any instructions directing Claude toward untrusted networks.

## Availability and Future Direction

Supported across Claude.ai, Claude Code, Claude Agent SDK, and Claude Developer Platform. Future plans include features for the full lifecycle of creating, editing, discovering, sharing, and using skills—including agents creating and evaluating their own skills.
