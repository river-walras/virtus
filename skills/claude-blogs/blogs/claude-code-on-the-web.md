# Claude Code on the web

**Source:** https://claude.com/blog/claude-code-on-the-web  
**Published:** October 20, 2025  
**Categories:** Product announcements, Claude Code

## Overview

Claude Code on the web lets users delegate coding tasks directly from the browser. Now in beta as a research preview, users can assign multiple coding tasks to Claude running on Anthropic-managed cloud infrastructure.

## Key Features

**Parallel Task Execution**: Run multiple tasks in parallel across different repositories from a single interface. Sessions run in isolated environments with real-time progress tracking, allowing active steering of Claude's work. Automatic PR creation ships faster.

**Workflow Flexibility**: Best for:
- Understanding project architecture and repository mapping
- Bug fixes and well-defined routine tasks
- Backend changes using test-driven development

Mobile support via iOS app for early-stage exploration.

## Security

Tasks execute in sandboxed environments with network and filesystem restrictions. Git interactions handled through a secure proxy ensuring Claude only accesses authorized repositories. Custom network configuration specifies which domains Claude Code can reach.

## Availability

Available in research preview for Pro and Max users at claude.com/code. Expanded (November 12, 2025) to Team and Enterprise users with premium seats, enabled by default with admin toggle controls.

Cloud-based sessions share rate limits with other Claude Code usage.
