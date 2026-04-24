# Introducing web search on the Anthropic API

**Source:** https://claude.com/blog/web-search-api  
**Published:** May 7, 2025  
**Categories:** Product announcements, Claude Platform

## Overview

Web search functionality on the Anthropic API enables Claude to access current information from the internet, letting developers build AI applications and agents with up-to-date insights and source citations.

## Core Functionality

Activate the web search tool in Messages API requests. Claude determines when searching would improve accuracy, generates targeted queries, retrieves results, analyzes them, and provides comprehensive answers with citations. Supports multiple progressive searches where earlier findings inform subsequent queries.

## Use Cases

- **Financial services**: Real-time stock analysis, market trends, regulatory monitoring
- **Legal research**: Recent court decisions and regulatory updates
- **Developer tools**: Latest API documentation and technology releases
- **Productivity**: Company reports and competitive intelligence

## Control Features

All web-sourced responses include citations for verification. Administrators can implement:
- Domain allow lists (approved sources)
- Domain block lists (preventing sensitive content access)
- Organization-level permission settings

## Integration with Claude Code

Web search is also available in Claude Code, providing access to current documentation and technical articles for working with evolving frameworks and troubleshooting issues.

## Availability and Pricing

Available for Claude 3.7 Sonnet, upgraded Claude 3.5 Sonnet, and Claude 3.5 Haiku.  
**Pricing**: $10 per 1,000 searches plus standard token costs.

Also supports a web fetch tool for analyzing specific webpage content.
