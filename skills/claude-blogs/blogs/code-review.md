# Bringing Code Review to Claude Code

**Source:** https://claude.com/blog/code-review  
**Published:** March 9, 2026  
**Categories:** Claude Code, Coding

## Overview

Anthropic has launched Code Review, an AI-powered system that automatically reviews pull requests using multiple agents working in parallel. Available in research preview for Team and Enterprise customers.

## The Problem

Code output per engineer has grown 200% over the past year, making code review a significant bottleneck. Before implementing Code Review, only 16% of PRs at Anthropic received substantive review comments.

## How It Works

When a PR is opened, Code Review deploys a team of agents that:
- Examine code changes simultaneously
- Verify identified bugs to eliminate false positives
- Rank findings by severity
- Post a summary comment on the PR plus inline comments for specific issues

The system scales with PR complexity. Average review time is approximately 20 minutes.

## Results

- 54% of PRs now receive substantive comments (up from 16%)
- Large PRs (1,000+ lines): 84% generate findings, averaging 7.5 issues
- Small PRs (under 50 lines): 31% generate findings, averaging 0.5 issues
- Less than 1% of findings are marked incorrect by engineers

## Cost & Controls

Reviews cost $15–25 on average, scaling with PR size. Admins can control spending through monthly caps, repository-level permissions, and analytics dashboards.

## Getting Started

Enable Code Review in Claude Code settings, install the GitHub App, and select repositories for automatic reviews. No developer configuration required.
