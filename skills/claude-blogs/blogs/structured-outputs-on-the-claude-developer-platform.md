# Structured outputs on the Claude Developer Platform

**Source:** https://claude.com/blog/structured-outputs-on-the-claude-developer-platform  
**Published:** November 14, 2025  
**Categories:** Product announcements, Claude Platform

## Overview

The Claude Developer Platform now supports structured outputs for Claude Sonnet 4.5 and Opus 4.1, in public beta. This feature guarantees that API responses conform to specified JSON schemas or tool definitions, eliminating parsing errors and failed tool calls in production applications.

## Key Benefits

Works in two ways:
1. Through JSON schema definitions provided in API requests
2. Through predefined tool specifications that Claude's output automatically conforms to

Particularly valuable for:
- **Data extraction** from images and documents where downstream systems require consistent formats
- **Multi-agent architectures** where consistent communication between agents maintains system stability
- **Complex search tools** requiring multiple fields filled accurately

## Industry Adoption

OpenRouter highlighted the feature's importance, noting it addresses a significant gap in agentic workflows where consistent data handling is essential for reliable agent operation.

## Availability

Currently in public beta for Sonnet 4.5 and Opus 4.1. Support for Haiku 4.5 coming soon.
