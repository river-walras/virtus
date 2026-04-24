# Understand Claude Code's Impact with Contribution Metrics

**Source:** https://claude.com/blog/contribution-metrics  
**Published:** January 29, 2026  
**Categories:** Claude Code, Coding

## Overview

Anthropic has launched contribution metrics in Claude Code's public beta, enabling engineering teams to measure how the AI tool impacts development velocity by tracking pull requests merged and code committed.

## Key Findings from Anthropic

Internal data shows a **67% increase in PRs merged per engineer per day** as Claude Code adoption increased. Between 70–90% of code is now written with Claude Code assistance across various teams.

## Metrics Capabilities

Integrates with GitHub to surface:
- **Pull requests merged** (with and without Claude Code assistance)
- **Lines of code committed** (comparing assisted vs. unassisted contributions)
- **Per-user adoption patterns** across teams

The system calculates metrics conservatively, counting only code where there is "high confidence in Claude Code's involvement."

## Implementation

1. Install the Claude GitHub App for your organization
2. Navigate to Admin settings and toggle GitHub Analytics on
3. Authenticate to the GitHub organization

Metrics populate automatically, appearing in the existing analytics dashboard accessible to workspace admins and owners.

## Availability

Available in beta for Claude Team and Enterprise customers.
