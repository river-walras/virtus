# Customize Claude Code with Plugins

**Source:** https://claude.com/blog/claude-code-plugins  
**Published:** October 9, 2025  
**Categories:** Product announcements, Claude Code

## Overview

Claude Code now supports plugins—custom collections of slash commands, agents, MCP servers, and hooks that install with a single command via `/plugin`.

## What Plugins Bundle

- **Slash commands**: Custom shortcuts for frequently-used operations
- **Subagents**: Purpose-built agents for specialized development tasks
- **MCP servers**: Tools and data source connections via Model Context Protocol
- **Hooks**: Customizations for key points in Claude Code's workflow

Plugins can be toggled on and off, reducing system prompt context when specific capabilities aren't needed.

## Use Cases

- **Enforcing standards**: Leaders maintain consistency through hooks for code reviews and testing
- **Supporting users**: Maintainers provide slash commands for correct package usage
- **Sharing workflows**: Distribute productivity-enhancing setups like debugging tools and deployment pipelines
- **Connecting tools**: Link internal tools via MCP servers using security protocols
- **Bundling customizations**: Framework authors package multiple related features

## Plugin Marketplaces

Anyone can build and host plugins in curated marketplaces. Hosting requires a git repo or URL with a properly formatted `.claude-plugin/marketplace.json` file.

Community examples: Dan Ávila's marketplace (DevOps automation, testing suites), Seth Hobson's repository (80+ specialized sub-agents).

Anthropic provides example plugins for PR reviews, security guidance, Claude Agent SDK development, and plugin creation itself.

## Getting Started

Now in public beta for all Claude Code users. Works across terminal and VS Code.

```
/plugin marketplace add anthropics/claude-code
/plugin install feature-dev
```
