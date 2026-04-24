# Introducing Agent Skills

**Source:** https://claude.com/blog/skills  
**Published:** October 16, 2025  
**Categories:** Product announcements, Claude Platform

## Overview

Claude now supports Skills—specialized folders containing instructions, scripts, and resources that enhance Claude's performance on specific tasks. Claude automatically identifies and loads relevant skills when needed.

## Key Properties

- **Composable**: Multiple skills work together, with Claude automatically coordinating their use
- **Portable**: Skills function consistently across Claude apps, Claude Code, and the API
- **Efficient**: Only essential information loads when relevant to the task
- **Powerful**: Skills can include executable code for tasks better suited to traditional programming

## Availability Across Products

**Claude Apps**: Pro, Max, Team, and Enterprise users can access skills for common tasks. Enabled via Settings; admins manage organization-wide access for Team and Enterprise.

**API/Developer Platform**: New `/v1/skills` endpoint for programmatic control over custom skill versioning. Requires Code Execution Tool beta.

**Claude Code**: Skills extend capabilities through the `anthropics/skills` marketplace via plugins. Users can also manually install skills in `~/.claude/skills`.

## Getting Started

Documentation, API docs, and customizable example skills available on GitHub. Enterprise users: expect simplified creation workflows and deployment capabilities in future releases.

## Partners

Box, Canva, Notion, and Rakuten are leveraging skills to streamline specialized workflows and enhance agentic capabilities.
