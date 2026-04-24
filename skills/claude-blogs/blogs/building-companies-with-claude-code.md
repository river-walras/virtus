# How three YC startups built their companies with Claude Code

**Source:** https://claude.com/blog/building-companies-with-claude-code  
**Published:** November 17, 2025  
**Categories:** Claude Code

## Overview

Three Y Combinator startups demonstrate how Claude Code is transforming how startups build and scale, compressing development cycles from weeks to hours.

## HumanLayer (F24): From SQL agents to scaling AI-first engineering teams

Dexter Horthy built HumanLayer—an API and SDK enabling AI agents to contact humans for feedback and approvals across multiple channels. After publishing "12-Factor Agents" (which went viral), the team built **CodeLayer** to help teams run multiple Claude agent sessions in parallel using worktrees and remote cloud workers.

"Once you have multiple people on your team shipping AI-written code, you have a completely different type of problem."

## Ambral (W25): Building production systems with subagents

Jack Stettner's AI-powered account management platform uses a precise model-specific workflow:
1. **Research phase (Opus 4.1)**: Deep research and comprehensive documentation
2. **Planning phase (Opus 4.1)**: Create discrete implementation phases in markdown
3. **Implementation phase (Sonnet 4.5)**: Execute each phase systematically

"Sonnet 4.5 has been absolutely killer in terms of implementing plans I create in Markdown."

## Vulcan Technologies (S25): Empowering non-technical founders

Tanner Jones and Aleksander Mekhanik (neither with traditional engineering backgrounds) used Claude to tackle regulatory code complexity. Their AI-powered regulatory analysis helped reduce Virginia's average new home price by $24,000, saving Virginians over $1 billion annually.

"If you understand language and critical thinking, you can use Claude Code well."

In 4 months, with 3 founders (only 1 technical), they secured state and federal government contracts and raised an **$11M seed round**.

## Best Practices from YC Founders

1. **Separate research, planning, and implementation** into discrete sessions
2. **Be deliberate about context management**: contradictions in prompt lead to low-quality output
3. **Monitor and interrupt the chain of thought**: have your finger on the trigger to escape bad behavior
