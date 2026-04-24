# Claude Agent SDK — Reference Index

> Quick navigation for all SDK documentation. Use this to find the right reference before diving in.

---

## Start Here

| File | What it answers |
|------|----------------|
| [Agent SDK/Overview.md](references/Agent%20SDK/Overview.md) | What is the Agent SDK, how does it compare to the Client SDK/CLI, branding rules |
| [Agent SDK/Quickstart.md](references/Agent%20SDK/Quickstart.md) | Install, set API key, build your first bug-fixing agent in Python or TypeScript |

---

## Core Concepts

| File | What it answers |
|------|----------------|
| [Core concepts/How_the_agent_loop_works.md](references/Core%20concepts/How_the_agent_loop_works.md) | Message lifecycle, tool execution order, context window, message types (`SystemMessage`, `AssistantMessage`, `ResultMessage`) |
| [Core concepts/Work_with_sessions.md](references/Core%20concepts/Work_with_sessions.md) | `continue`, `resume`, `fork` — how to persist and branch conversations; `ClaudeSDKClient` vs standalone `query()` |
| [Core concepts/Use_claude_code_features.md](references/Core%20concepts/Use_claude_code_features.md) | Using `CLAUDE.md`, skills, slash commands, and plugins from within the SDK |

---

## Input & Output

| File | What it answers |
|------|----------------|
| [Input and output/Stream_responses_in real_time.md](references/Input%20and%20output/Stream_responses_in%20real_time.md) | Consuming streamed assistant messages; filtering noise from system/tool messages |
| [Input and output/Streaming_input.md](references/Input%20and%20output/Streaming_input.md) | Sending live/streaming input (e.g., typing indicators, incremental prompts) |
| [Input and output/Get_structured_output_from_agents.md](references/Input%20and%20output/Get_structured_output_from_agents.md) | `outputFormat` / `output_format` with JSON Schema, Zod (TS), Pydantic (Python) for typed results |
| [Input and output/Handle_approvals_and_user _input.md](<references/Input%20and%20output/Handle_approvals_and_user%20_input.md>) | `canUseTool` callback; prompting users for permission; handling `AskUserQuestion` |

---

## Extend with Tools

| File | What it answers |
|------|----------------|
| [Extend with tools/give_claude_custom_tools.md](references/Extend%20with%20tools/give_claude_custom_tools.md) | `@tool` / `tool()` decorator; `createSdkMcpServer`; returning images/errors; tool annotations |
| [Extend with tools/connect_to_external_tools_with_mcp.md](references/Extend%20with%20tools/connect_to_external_tools_with_mcp.md) | Connecting external MCP servers (Playwright, databases, APIs) via `mcpServers` option |
| [Extend with tools/Subagents_in_the_SDK.md](references/Extend%20with%20tools/Subagents_in_the_SDK.md) | `AgentDefinition`; parallel subagents; context isolation; resuming subagents; tool restrictions |
| [Extend with tools/scale_to_many_tools_with_tool_search.md](references/Extend%20with%20tools/scale_to_many_tools_with_tool_search.md) | Deferred tool loading; tool search when you have 50+ tools |

---

## Control & Observability

| File | What it answers |
|------|----------------|
| [Control and observability/Configure_permissions.md](references/Control%20and%20observability/Configure_permissions.md) | Permission modes (`acceptEdits`, `dontAsk`, `bypassPermissions`); `allowedTools` / `disallowedTools`; evaluation order |
| [Control and observability/Intercept_and_control_agent_behavior_with_hooks.md](references/Control%20and%20observability/Intercept_and_control_agent_behavior_with_hooks.md) | `PreToolUse`, `PostToolUse`, `Stop` hooks; blocking/modifying tool calls; audit logging |
| [Control and observability/Observability_with_OpenTelemetry.md](references/Control%20and%20observability/Observability_with_OpenTelemetry.md) | Tracing, spans, and metrics with OpenTelemetry |
| [Control and observability/Track_cost_and_usage.md](references/Control%20and%20observability/Track_cost_and_usage.md) | `total_cost_usd`, token counts from `ResultMessage`; budget limits |
| [Control and observability/Rewind_file_changes_with_checkpointing.md](references/Control%20and%20observability/Rewind_file_changes_with_checkpointing.md) | Snapshotting and reverting filesystem changes across sessions |
| [Control and observability/Todo_Lists.md](references/Control%20and%20observability/Todo_Lists.md) | Using the built-in `TodoWrite` / `TodoRead` task list tools |

---

## Customize Behavior

| File | What it answers |
|------|----------------|
| [Customize behavior/Modifying_system_prompts.md](references/Customize%20behavior/Modifying_system_prompts.md) | `systemPrompt` option (custom / preset / append); `CLAUDE.md` integration; `settingSources` |
| [Customize behavior/Agent_skills_in_the_sdk.md](references/Customize%20behavior/Agent_skills_in_the_sdk.md) | Defining skills as `.claude/skills/*/SKILL.md`; loading them with `settingSources` |
| [Customize behavior/Slash_commands_in_the_sdk.md](references/Customize%20behavior/Slash_commands_in_the_sdk.md) | Custom slash commands from `.claude/commands/*.md` |
| [Customize behavior/Plugins_in_the_sdk.md](references/Customize%20behavior/Plugins_in_the_sdk.md) | Programmatic plugins; bundling agents, MCP servers, and commands together |

---

## Deployment

| File | What it answers |
|------|----------------|
| [Deployment/Hosting_the_Agent_SDK.md](references/Deployment/Hosting_the_Agent_SDK.md) | Container requirements, resource allocation, sandbox providers (Modal, E2B, Fly, etc.) |
| [Deployment/Securely_deploying_AI_agents.md](references/Deployment/Securely_deploying_AI_agents.md) | Network controls, credential management, isolation technologies |

---

## SDK API Reference

| File | What it answers |
|------|----------------|
| [SDK references/Agent_SDK_reference_Python.md](references/SDK%20references/Agent_SDK_reference_Python.md) | Full Python API: `query()`, `ClaudeSDKClient`, `ClaudeAgentOptions`, all types |
| [SDK references/Agent_SDK_reference_TypeScript.md](references/SDK%20references/Agent_SDK_reference_TypeScript.md) | Full TypeScript API: `query()`, `Options`, all types and interfaces |
| [SDK references/Migrate_to_Claude_Agent_SDK.md](references/SDK%20references/Migrate_to_Claude_Agent_SDK.md) | Migrating from the old Claude Code SDK to the Claude Agent SDK |
| [SDK references/TypeScript_SDK_V2_interface_preview.md](references/SDK%20references/TypeScript_SDK_V2_interface_preview.md) | Preview of the V2 TypeScript interface (`createSession`, `send`/`stream` pattern) |

---

## Built-in Tools Quick Reference

| Tool | What it does |
|------|-------------|
| `Read` | Read any file |
| `Write` | Create new files |
| `Edit` | Make precise edits to existing files |
| `Bash` | Run terminal commands |
| `Glob` | Find files by pattern (`**/*.ts`) |
| `Grep` | Search file contents with regex |
| `WebSearch` | Search the web |
| `WebFetch` | Fetch and parse a web page |
| `AskUserQuestion` | Ask the user a clarifying question |
| `Agent` | Spawn a subagent |
| `Monitor` | Watch a background script, react to each output line |
| `TodoWrite` / `TodoRead` | Manage a task list |
