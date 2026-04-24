# Using CLAUDE.md files: Customizing Claude Code for your codebase

**Source:** https://claude.com/blog/using-claude-md-files  
**Published:** November 25, 2025  
**Categories:** Claude Code

## Overview

CLAUDE.md files provide persistent context to Claude Code about your project structure, coding standards, and workflows. Rather than repeatedly explaining your codebase's architecture and conventions, document this information once in a configuration file that Claude automatically incorporates into every conversation.

## What is a CLAUDE.md File?

A special configuration document placed in your repository (root directory, parent directories for monorepos, or home folder) that becomes part of Claude's system prompt.

Essential sections:
- Project summary and purpose
- Key directory structure and organization
- Coding standards and style guidelines
- Development commands and workflows
- Testing requirements and procedures
- Project-specific conventions and warnings

## Getting Started with /init

The `/init` command automates CLAUDE.md creation by analyzing your codebase—examining project structure, configuration files, and existing documentation to generate a starter configuration.

After generation:
- Review the output for accuracy
- Add workflow instructions Claude couldn't infer
- Remove generic guidance inapplicable to your project
- Commit to version control for team benefit

## Structuring Your CLAUDE.md

**Architectural Context**: Include project summaries, high-level directory trees, primary dependencies, and architectural patterns.

**Connect to Your Tools**: Document custom tools, scripts, and MCP servers your team uses with usage examples.

**Define Standard Workflows**: Establish workflows Claude should follow before making code changes.

## Additional Best Practices

- Use `/clear` between distinct tasks to reset context while preserving CLAUDE.md configuration
- Leverage subagents for distinct work phases requiring different perspectives
- Create custom commands in `.claude/commands/` directory for repetitive prompts
- Avoid including sensitive information like API keys

CLAUDE.md should reflect your team's actual development practices rather than theoretical best practices.
