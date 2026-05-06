# Building agents that reach production systems with MCP

**Source:** https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp  
**Published:** April 22, 2026  
**Categories:** Agents, Claude Platform

## Overview

This post compares three ways to connect agents to external systems: direct API calls, command-line interfaces, and Model Context Protocol (MCP). It argues that production cloud agents increasingly need MCP because it gives them a portable, authenticated, semantically rich layer for reaching real systems.

## Integration Options

### Direct API calls

Direct calls work for one-off integrations, but each agent-service pair becomes bespoke at scale. Auth, tool descriptions, and edge cases multiply across agents and services.

### CLIs

Command-line tools are fast for local or sandboxed environments, but they assume filesystem and shell access and are poorly suited to web, mobile, or cloud-hosted agents.

### MCP

MCP exposes capabilities through a common protocol. A remote MCP server can serve compatible clients across different deployment environments, with standardized auth, discovery, and richer semantics.

## MCP Server Patterns

- Build remote servers for maximum reach.
- Group tools around user intent instead of mirroring every endpoint.
- For very large APIs, expose a thin code-execution surface rather than thousands of tools.
- Use MCP Apps for interactive charts, forms, dashboards, and inline UI.
- Use elicitation to ask for missing inputs or confirm sensitive actions.
- Lean on standardized OAuth and Claude Managed Agents vaults for cloud auth.

## Context Efficiency

The post recommends tool search and programmatic tool calling to reduce tool-definition and result tokens. It reports that tool search can reduce tool-definition tokens by more than 85%, while programmatic tool calling can reduce token usage on complex workflows by roughly 37%.

## Skills and MCP

MCP provides tool and data access; skills provide procedural expertise. Anthropic recommends bundling MCP servers with skills as plugins, or distributing skills alongside MCP servers so agents understand how to use the integration well.

## When to Use This Blog

Use this source for questions about MCP vs APIs vs CLIs, cloud-hosted agents, remote MCP server design, MCP auth, MCP Apps, tool search, programmatic tool calling, and combining MCP with skills.
