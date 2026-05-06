---
name: claude-blogs
description: "Answer questions about Claude and Anthropic products using official claude.com/blog posts as a knowledge base, and refresh the local blog cache when current coverage matters. USE when: user asks how Claude Code works, asks about Claude features (MCP, skills, artifacts, prompt caching, tool use, web search, context windows), asks about Claude plans or pricing, asks about Claude integrations (Slack, Microsoft 365, Amazon Bedrock), asks for enterprise AI use cases or case studies, asks about agent skills or multi-agent systems, asks about best practices for prompting or building with Claude, asks for latest/newest/current Claude blog information, or asks to update/fetch/refresh the Claude blog index. NOT USE when: user is asking about a non-Claude AI product or provider, asking general programming questions unrelated to Claude, asking about Anthropic safety research or model internals not covered in blog posts, or the question can be answered from existing conversation context without needing blog references."
---

# Claude Blog Knowledge Base

You have access to 130 official claude.com/blog posts saved as markdown files in the `blogs/` directory of this skill.

## How to Use This Skill

When answering a question about Claude, Claude Code, or Anthropic products:

1. **Refresh first when recency matters.** If the user asks for latest/newest/current information, or asks to update/fetch/refresh the blog cache, run `scripts/update_blogs.py` from this skill directory before consulting the index. If the environment requires network approval, ask the user to allow the update. If the user declines or the refresh fails, continue from the local cache and clearly say the answer may not include the newest blog posts.
2. **Consult the index** at `index.md` to identify which blog files are most relevant to the question.
3. **Read the relevant blog files** from the `blogs/` directory.
4. **Answer based on the blog content**, citing the source blog and its URL.

## Refresh Workflow

Run the updater from the skill root:

```bash
python3 scripts/update_blogs.py
```

The updater fetches the official `https://claude.com/blog` listing, creates markdown files for newly listed posts, prepends new URLs to `urls.txt`, updates post counts in `SKILL.md` and `index.md`, and maintains the auto-generated "Recently Fetched Posts" block in `index.md`.

Use `--dry-run` to preview changes and `--force` to regenerate markdown for posts currently visible on the blog listing.

Do not ask to refresh for stable, non-recency questions when the local cache is sufficient.

## Index Summary

The index (`index.md`) organizes 130 blogs into these categories:

- **Claude Code — Getting Started**: CLAUDE.md files, hooks, subagents, web and desktop versions, sandboxing, PR workflows
- **Claude Code — Tasks**: Debugging, API integration, performance optimization, code review, security reviews, prompt caching, legacy onboarding
- **Claude Code — Plugins**: Plugin system, remote MCP in Claude Code
- **Claude Code — Enterprise**: Admin controls, metrics, trends in software development
- **Agent Skills**: What skills are, how to build them, best practices, testing, Claude API skill distribution
- **Multi-Agent Systems**: When to use multi-agent, coordination patterns, Claude Agent SDK
- **Model Context Protocol (MCP)**: What MCP is, production MCP integrations, connectors, integrations (Jira, Zapier, etc.)
- **Enterprise AI**: Enterprise transformation, case studies across industries
- **Financial Services**: AI agents in finance, Claude deployment in finance, Kepler, Brex, fraud detection
- **Healthcare**: AI agents in healthcare, Pfizer, Novo Nordisk
- **Security**: AI-accelerated threats, Claude Security, Chrome extension security, sandboxing
- **Claude Platform API**: Prompt caching, token-saving, context management, web search API, tool use, Citations API, structured outputs, 1M context, fine-tuning
- **Developer Console**: Upgraded Console, prompt evaluation, prompt improver, prompt generator
- **Claude Apps**: Artifacts, file creation, interactive tools, Research feature, web search
- **Enterprise Plans**: Claude for Enterprise, Team plan, Cowork, Cowork deployment, Workspaces
- **Integrations**: Slack, Microsoft 365, Microsoft 365 Copilot, connectors directory, everyday connectors, FedRAMP
- **Models & Pricing**: Max plan, Android app, Amazon Bedrock history
