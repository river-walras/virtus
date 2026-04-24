# Extending Claude's capabilities with skills and MCP servers

**Source:** https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers  
**Published:** December 19, 2025  
**Categories:** Agents, Claude apps

## Overview

Skills and Model Context Protocol (MCP) servers work together to enable Claude to follow organizational workflows effectively. MCP provides connectivity to external tools and data; skills teach Claude how to use those connections strategically.

## Understanding the Relationship

Think of MCP as access to a hardware store's inventory—it provides the tools. Skills are like having an expert employee who knows which items you need and how to use them properly.

## Key Differences

**MCP servers:**
- Enable real-time data access and external actions
- Connect to platforms like GitHub, Salesforce, and Notion
- Load upfront and remain available
- Handle connectivity and API integration

**Skills:**
- Teach procedural workflows and methodology
- Load on-demand when relevant
- Preserve token context
- Encode institutional knowledge

## When to Use Each

Choose **skills** for multi-step workflows requiring consistency, domain expertise, and processes with mandatory standards.

Choose **MCP servers** for real-time data access, external system actions, or API integrations.

## Real-World Examples

Financial analysts use comparable company analysis skills combined with MCP connections to S&P Capital IQ and Morningstar to automate valuations while maintaining compliance standards.

Meeting prep workflows leverage Notion's Meeting Intelligence skill with MCP connections to discover relevant pages, structure documents, and save outputs.

## Getting Started

Enable skills in Settings on claude.ai, browse the skills library, and connect MCP servers to your tools.
