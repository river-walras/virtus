# Onboarding Claude Code like a new developer: Lessons from 17 years of development

**Source:** https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development  
**Published:** April 28, 2026  
**Categories:** Claude Code

## Overview

This post describes how Brendan MacLean of the University of Washington's MacCoss Lab onboarded Claude Code to Skyline, a 700,000+ line C# protein-analysis codebase maintained since 2008.

## Context as an Artifact

MacLean treated Claude Code like a new developer. He created a separate `pwiz-ai` repository for AI context that applies across branches and time, with a `CLAUDE.md` for orientation and skills for domain-specific expertise.

## Skills

The lab uses skills to encode project knowledge and workflows. Examples include:

- A Skyline development skill for project orientation
- A version-control skill for project commit and PR conventions
- A debugging skill that pushes Claude toward root cause analysis before fixes

## Results

Claude Code helped finish a Files View panel that had been stalled after its owner left, revive an old nightly test management module, automate screenshot reproduction for 2,000+ tutorial images, and build MCP servers to expose test failures, exceptions, support threads, and GitHub release data.

## Advice

MacLean recommends maintaining versioned context, investing in a skill library, and building MCP integrations when Claude needs real project data. For open source projects, durable context helps preserve institutional memory across contributor turnover.

## When to Use This Blog

Use this source for Claude Code onboarding, large legacy codebases, `CLAUDE.md`, skills, MCP integrations, project context repositories, and open-source maintainer workflows.
