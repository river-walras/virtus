# Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

**Source:** https://claude.com/blog/skills-explained  
**Published:** November 13, 2025  
**Categories:** Agents, Claude apps

## Understanding Your Agentic Building Blocks

### Skills
Folders containing instructions, scripts, and resources that Claude discovers and loads dynamically when relevant. Use progressive disclosure (~100 token metadata first, then full instructions ≤5,000 tokens, then files on demand).

**Best for:** Organizational workflows, domain expertise, personal preferences.

### Prompts
Natural language instructions provided during a conversation. Ephemeral, conversational, reactive.

**Best for:** One-off requests, conversational refinement, immediate context analysis.

### Projects
Self-contained workspaces with independent chat histories and knowledge bases (200K token context window). Available on all paid plans.

**Best for:** Persistent context, workspace organization, team collaboration.

### Subagents
Specialized AI assistants with independent context windows, custom system prompts, and specific tool permissions. Available in Claude Code and the Claude Agent SDK.

**Best for:** Task specialization, context management, parallel processing, tool restriction.

### MCP (Model Context Protocol)
Open standard for connecting AI assistants to external systems—content repositories, business tools, databases.

**Best for:** Accessing external data, using business tools, connecting to development environments.

## Comparison Matrix

| Feature | Skills | Prompts | Projects | Subagents | MCP |
|---------|--------|---------|----------|-----------|-----|
| Persistence | Across conversations | Single conversation | Within project | Across sessions | Continuous connection |
| Contains | Instructions + code + assets | Natural language | Documents + context | Full agent logic | Tool definitions |
| When it loads | Dynamically, as needed | Each turn | Always in project | When invoked | Always available |

## How They Work Together

Building a research agent: **Project** stores background knowledge → **MCP** connects to Google Drive and GitHub → **Skills** encode research methodology → **Subagents** execute specialized tasks independently.

## Common Questions

- **Skills vs. prompts**: Use prompts for one-time instructions; Skills for procedures you'll repeat
- **Skills vs. Projects**: Projects say "here's what you need to know"; Skills say "here's how to do things"
- **MCP vs. Skills**: MCP connects Claude to data; Skills teach Claude how to use that data
