---
name: claude-blogs
description: "Answer questions about Claude and Anthropic products using official claude.com/blog posts as a knowledge base. USE when: user asks how Claude Code works, asks about Claude features (MCP, skills, artifacts, prompt caching, tool use, web search, context windows), asks about Claude plans or pricing, asks about Claude integrations (Slack, Microsoft 365, Amazon Bedrock), asks for enterprise AI use cases or case studies, asks about agent skills or multi-agent systems, asks about best practices for prompting or building with Claude. NOT USE when: user is asking about a non-Claude AI product or provider, asking general programming questions unrelated to Claude, asking about Anthropic safety research or model internals not covered in blog posts, or the question can be answered from existing conversation context without needing blog references."
---

# Claude Blog Knowledge Base

You have access to 114 official claude.com/blog posts saved as markdown files in the `blogs/` directory of this skill.

## How to Use This Skill

When answering a question about Claude, Claude Code, or Anthropic products:

1. **Consult the index** at `index.md` to identify which blog files are most relevant to the question
2. **Read the relevant blog files** from the `blogs/` directory
3. **Answer based on the blog content**, citing the source blog and its URL

## Index Summary

The index (`index.md`) organizes 114 blogs into these categories:

- **Claude Code — Getting Started**: CLAUDE.md files, hooks, subagents, web version, sandboxing, PR workflows
- **Claude Code — Tasks**: Debugging, API integration, performance optimization, code review, security reviews
- **Claude Code — Plugins**: Plugin system, remote MCP in Claude Code
- **Claude Code — Enterprise**: Admin controls, metrics, trends in software development
- **Agent Skills**: What skills are, how to build them, best practices, testing
- **Multi-Agent Systems**: When to use multi-agent, coordination patterns, Claude Agent SDK
- **Model Context Protocol (MCP)**: What MCP is, connectors, integrations (Jira, Zapier, etc.)
- **Enterprise AI**: Enterprise transformation, case studies across industries
- **Financial Services**: AI agents in finance, Brex, fraud detection
- **Healthcare**: AI agents in healthcare, Pfizer, Novo Nordisk
- **Security**: AI-accelerated threats, Chrome extension security, sandboxing
- **Claude Platform API**: Prompt caching, token-saving, context management, web search API, tool use, Citations API, structured outputs, 1M context, fine-tuning
- **Developer Console**: Upgraded Console, prompt evaluation, prompt improver, prompt generator
- **Claude Apps**: Artifacts, file creation, interactive tools, Research feature, web search
- **Enterprise Plans**: Claude for Enterprise, Team plan, Cowork, Workspaces
- **Integrations**: Slack, Microsoft 365, Microsoft 365 Copilot, connectors directory, FedRAMP
- **Models & Pricing**: Max plan, Android app, Amazon Bedrock history
