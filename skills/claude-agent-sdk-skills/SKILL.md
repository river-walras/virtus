---
name: agent-sdk-builder
description: Build, debug, extend, or deploy Claude Agent SDK agents in Python or TypeScript. Use this skill whenever someone mentions the Claude Agent SDK, agent loops, query(), ClaudeAgentOptions, subagents, hooks, MCP servers in the context of the Agent SDK, structured output from agents, multi-turn sessions with resume/fork, deployment of SDK agents to production, or migrating from the old Claude Code SDK. Covers installation, quickstart, message streaming, sessions, custom tools, permissions, observability, and production deployment.
---

# Skill: Claude Agent SDK Builder

> When the user wants to build an agent with the Claude Agent SDK — whether that's writing their first `query()`, wiring up hooks, adding subagents, or deploying to production — follow the steps in this skill to diagnose their intent, surface the right reference, and produce working code.

---

## How to Use This Skill

**Trigger:** User asks about building, debugging, or extending a Claude Agent SDK agent (Python or TypeScript).

**Process:**
1. Identify the user's goal using the [Intent Classifier](#intent-classifier) below.
2. Read the reference file(s) listed for that goal — they are in `references/` and indexed in `INDEX.md`.
3. Produce a working code snippet in the user's language (Python or TypeScript). Default to Python if unspecified.
4. Point the user to the exact reference section for deeper reading.

---

## Intent Classifier

Match the user's goal to one of these categories, then follow the linked recipe.

| User says… | Category | Recipe |
|------------|----------|--------|
| "Get started", "first agent", "install", "quickstart" | **Bootstrap** | [→ Bootstrap a New Agent](#recipe-bootstrap-a-new-agent) |
| "Stream output", "print Claude's thinking", "handle messages" | **Message Handling** | [→ Handle the Message Stream](#recipe-handle-the-message-stream) |
| "Multi-turn", "continue conversation", "remember context", "follow-up" | **Sessions** | [→ Multi-Turn Sessions](#recipe-multi-turn-sessions) |
| "Custom tool", "call my API", "function tool", "database tool" | **Custom Tools** | [→ Add a Custom Tool](#recipe-add-a-custom-tool) |
| "MCP", "external server", "Playwright", "browser" | **MCP** | [→ Connect an MCP Server](#recipe-connect-an-mcp-server) |
| "Subagent", "parallel agents", "delegate", "specialist agent" | **Subagents** | [→ Define Subagents](#recipe-define-subagents) |
| "Hook", "block", "audit", "log tool calls", "intercept" | **Hooks** | [→ Use Hooks](#recipe-use-hooks) |
| "Permission", "approve", "deny", "canUseTool", "user approval" | **Permissions** | [→ Configure Permissions](#recipe-configure-permissions) |
| "Structured output", "JSON result", "typed response", "Pydantic", "Zod" | **Structured Output** | [→ Get Structured Output](#recipe-get-structured-output) |
| "System prompt", "customize behavior", "CLAUDE.md", "persona" | **System Prompt** | [→ Customize the System Prompt](#recipe-customize-the-system-prompt) |
| "Cost", "tokens", "budget", "usage tracking" | **Observability** | [→ Track Cost and Usage](#recipe-track-cost-and-usage) |
| "OpenTelemetry", "traces", "spans", "Honeycomb", "Datadog", "otel" | **Tracing** | [→ OpenTelemetry Tracing](#recipe-opentelemetry-tracing) |
| "Checkpoint", "rewind", "undo", "restore files", "rollback" | **Checkpointing** | [→ Rewind File Changes](#recipe-rewind-file-changes) |
| "Streaming input", "send image", "queue messages", "interrupt" | **Streaming Input** | [→ Stream Input Messages](#recipe-stream-input-messages) |
| "Too many tools", "tool search", "50 tools", "100 tools", "ENABLE_TOOL_SEARCH" | **Tool Search** | [→ Scale with Tool Search](#recipe-scale-with-tool-search) |
| "Skills in SDK", "load skill", "setting_sources", "use skill programmatically" | **Skills** | [→ Load Skills in the SDK](#recipe-load-skills-in-the-sdk) |
| "Deploy", "Docker", "production", "sandbox", "hosting" | **Deployment** | [→ Deploy to Production](#recipe-deploy-to-production) |
| "Migrate", "old SDK", "Claude Code SDK" | **Migration** | [→ Migrate from Old SDK](#recipe-migrate-from-old-sdk) |

---

## Recipe: Bootstrap a New Agent

**References:** `references/Agent SDK/Overview.md`, `references/Agent SDK/Quickstart.md`

### Install

```bash
# TypeScript
npm install @anthropic-ai/claude-agent-sdk

# Python (uv)
uv init && uv add claude-agent-sdk

# Python (pip)
pip install claude-agent-sdk
```

Set `ANTHROPIC_API_KEY` in your environment (or `.env` file).

### Minimal Working Agent

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async def main():
    async for message in query(
        prompt="List the files in this directory",
        options=ClaudeAgentOptions(
            allowed_tools=["Bash", "Glob"],
            permission_mode="acceptEdits",
        ),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
        elif isinstance(message, ResultMessage):
            print(f"Done ({message.subtype})")

asyncio.run(main())
```

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "List the files in this directory",
  options: {
    allowedTools: ["Bash", "Glob"],
    permissionMode: "acceptEdits",
  },
})) {
  if (message.type === "assistant") {
    for (const block of message.message.content) {
      if ("text" in block) console.log(block.text);
    }
  } else if (message.type === "result") {
    console.log(`Done (${message.subtype})`);
  }
}
```

**Key options to know:**
- `allowed_tools` — pre-approves specific tools (no prompt)
- `permission_mode` — `"acceptEdits"` auto-approves file ops; `"dontAsk"` denies anything not in `allowedTools`; `"bypassPermissions"` approves everything (use in sandboxes only)
- `system_prompt` — override Claude's default instructions
- `cwd` — working directory (defaults to current)

---

## Recipe: Handle the Message Stream

**Reference:** `references/Core concepts/How_the_agent_loop_works.md`

Every `query()` call yields a stream of typed messages. Here's what each type means:

| Python type | TS `message.type` | When it appears |
|-------------|-------------------|-----------------|
| `SystemMessage` (subtype `"init"`) | `"system"` / `"init"` | First message; contains `session_id` |
| `AssistantMessage` | `"assistant"` | Claude's text or tool calls |
| `UserMessage` (tool results) | `"user"` | Tool execution results fed back |
| `ResultMessage` | `"result"` | Final outcome (`success`, `error_*`) |

**Practical filter — only show what matters:**

```python
from claude_agent_sdk import AssistantMessage, ResultMessage, SystemMessage
from claude_agent_sdk.types import TextBlock, ToolUseBlock

async for message in query(prompt="...", options=options):
    if isinstance(message, SystemMessage) and message.subtype == "init":
        session_id = message.data["session_id"]

    elif isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text)          # Claude's reasoning
            elif isinstance(block, ToolUseBlock):
                print(f"[tool] {block.name}({block.input})")

    elif isinstance(message, ResultMessage):
        if message.subtype == "success":
            print(f"Result: {message.result}")
        else:
            print(f"Error: {message.subtype}")   # error_max_turns, etc.
```

**ResultMessage subtypes to handle:**
- `"success"` — task completed
- `"error_max_turns"` — hit turn limit; resume the session with a higher limit
- `"error_max_budget_usd"` — hit cost cap; resume or increase budget
- `"error_during_execution"` — tool or runtime error

---

## Recipe: Multi-Turn Sessions

**Reference:** `references/Core concepts/Work_with_sessions.md`

### One-process multi-turn (Python: `ClaudeSDKClient`)

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, ResultMessage
from claude_agent_sdk.types import TextBlock

async def main():
    async with ClaudeSDKClient(
        options=ClaudeAgentOptions(allowed_tools=["Read", "Glob"])
    ) as client:
        await client.query("Analyze the auth module")
        async for msg in client.receive_response():
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock): print(block.text)

        # Second query has full context from the first
        await client.query("Now suggest refactors for it")
        async for msg in client.receive_response():
            if isinstance(msg, ResultMessage):
                print(msg.result)

asyncio.run(main())
```

### One-process multi-turn (TypeScript: `continue: true`)

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const msg of query({ prompt: "Analyze the auth module", options: { allowedTools: ["Read", "Glob"] } })) {
  if (msg.type === "result") console.log(msg.result);
}

// continue: true resumes the most recent session in cwd
for await (const msg of query({ prompt: "Now suggest refactors", options: { continue: true } })) {
  if (msg.type === "result") console.log(msg.result);
}
```

### Resume a specific session by ID

```python
# Capture session_id from the first run
session_id = None
async for message in query(prompt="Analyze auth.py", options=ClaudeAgentOptions(...)):
    if isinstance(message, ResultMessage):
        session_id = message.session_id

# Resume later (even after process restart, if session file exists on same machine)
async for message in query(
    prompt="Now implement the changes you suggested",
    options=ClaudeAgentOptions(resume=session_id, allowed_tools=["Read", "Edit"]),
):
    if isinstance(message, ResultMessage):
        print(message.result)
```

### Fork to explore alternatives

```python
# Fork creates a new session from the same history; original is untouched
forked_id = None
async for message in query(
    prompt="Try OAuth2 instead of JWT",
    options=ClaudeAgentOptions(resume=session_id, fork_session=True),
):
    if isinstance(message, ResultMessage):
        forked_id = message.session_id
```

> **Tip:** Sessions are stored at `~/.claude/projects/<encoded-cwd>/*.jsonl`. To resume on a different machine, copy the session file to the same path.

---

## Recipe: Add a Custom Tool

**Reference:** `references/Extend with tools/give_claude_custom_tools.md`

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, tool, create_sdk_mcp_server

@tool(
    "search_docs",
    "Search internal documentation for a keyword",
    {"query": str, "limit": int},          # simple type map → JSON Schema
)
async def search_docs(args):
    results = my_search_index.search(args["query"], limit=args["limit"])
    return {
        "content": [{"type": "text", "text": "\n".join(results)}]
    }

# Wrap in an in-process MCP server (no separate process needed)
mcp_server = create_sdk_mcp_server([search_docs])

async def main():
    async for message in query(
        prompt="Find docs about authentication",
        options=ClaudeAgentOptions(
            mcp_servers={"my-tools": mcp_server},
            allowed_tools=["search_docs"],         # pre-approve it
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

**Error handling — let Claude react to failures:**
```python
async def my_tool(args):
    try:
        result = risky_operation(args["input"])
        return {"content": [{"type": "text", "text": result}]}
    except Exception as e:
        return {
            "content": [{"type": "text", "text": str(e)}],
            "isError": True,   # Claude sees this and can retry or report
        }
```

---

## Recipe: Connect an MCP Server

**Reference:** `references/Extend with tools/connect_to_external_tools_with_mcp.md`

```python
options = ClaudeAgentOptions(
    mcp_servers={
        # stdio MCP server (runs as subprocess)
        "playwright": {"command": "npx", "args": ["@playwright/mcp@latest"]},
        # SSE / HTTP MCP server
        "my-api": {"url": "https://my-api.example.com/mcp"},
    }
)
```

```typescript
options: {
  mcpServers: {
    playwright: { command: "npx", args: ["@playwright/mcp@latest"] },
    "my-api": { url: "https://my-api.example.com/mcp" },
  }
}
```

Once connected, MCP tools are available to Claude the same as built-in tools. Pre-approve them with `allowedTools: ["mcp__playwright__navigate", ...]` or use a permission mode.

---

## Recipe: Define Subagents

**Reference:** `references/Extend with tools/Subagents_in_the_SDK.md`

Subagents run in isolated contexts — they don't inherit the parent's conversation history. Only their final message returns to the parent.

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async for message in query(
    prompt="Use the code-reviewer agent to review auth.py",
    options=ClaudeAgentOptions(
        # Agent tool is required — subagents are invoked through it
        allowed_tools=["Read", "Grep", "Glob", "Agent"],
        agents={
            "code-reviewer": AgentDefinition(
                description="Security-focused code reviewer. Use for auditing code quality and vulnerabilities.",
                prompt="""You are a security-focused code reviewer.
Identify vulnerabilities, anti-patterns, and unsafe practices.
Be specific: cite file paths and line numbers.""",
                tools=["Read", "Grep", "Glob"],   # read-only: cannot modify files
                model="opus",                      # override model per agent
            ),
        },
    ),
):
    if hasattr(message, "result"):
        print(message.result)
```

**Parallel subagents — run multiple at once:**
```python
prompt = """Run these three agents in parallel:
1. Use the style-checker agent to check code style
2. Use the security-scanner agent to find vulnerabilities
3. Use the test-runner agent to execute the test suite
Then synthesize their findings."""
```

**Rules:**
- Always include `"Agent"` in `allowed_tools` for the parent
- Never include `"Agent"` in a subagent's `tools` (subagents cannot spawn subagents)
- Write a clear `description` — Claude uses it to decide when to delegate automatically
- To force a specific subagent, name it explicitly in the prompt: "Use the X agent to..."

---

## Recipe: Use Hooks

**Reference:** `references/Control and observability/Intercept_and_control_agent_behavior_with_hooks.md`

Hooks intercept tool calls before (`PreToolUse`) or after (`PostToolUse`) execution.

### Block dangerous operations

```python
from claude_agent_sdk import ClaudeAgentOptions, HookMatcher

async def block_rm_rf(input_data, tool_use_id, context):
    command = input_data.get("tool_input", {}).get("command", "")
    if "rm -rf" in command:
        return {
            "hookSpecificOutput": {
                "hookEventName": input_data["hook_event_name"],
                "permissionDecision": "deny",
                "permissionDecisionReason": "rm -rf is not allowed",
            }
        }
    return {}   # empty dict = allow

options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [HookMatcher(matcher="Bash", hooks=[block_rm_rf])]
    }
)
```

### Audit log all file changes

```python
from datetime import datetime

async def audit_file_write(input_data, tool_use_id, context):
    file_path = input_data.get("tool_input", {}).get("file_path", "?")
    with open("audit.log", "a") as f:
        f.write(f"{datetime.now().isoformat()} WRITE {file_path}\n")
    return {}   # PostToolUse hooks cannot block; always return {}

options = ClaudeAgentOptions(
    hooks={
        "PostToolUse": [HookMatcher(matcher="Write|Edit", hooks=[audit_file_write])]
    }
)
```

**Available hook events:** `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`, `SessionEnd`, `UserPromptSubmit`  
**`matcher`** is a `|`-separated regex matched against the tool name. Omit to match all tools.

---

## Recipe: Configure Permissions

**Reference:** `references/Control and observability/Configure_permissions.md`

### Permission evaluation order (highest priority first)

1. **Hooks** (`PreToolUse`) — can allow, deny, or pass through
2. **Deny rules** (`disallowed_tools`) — always block, even in `bypassPermissions`
3. **Permission mode** — global default behavior
4. **Allow rules** (`allowed_tools`) — pre-approves listed tools
5. **`canUseTool` callback** — runtime user decision

### Permission mode cheat sheet

| Mode | Behavior | Use for |
|------|----------|---------|
| `"acceptEdits"` | Auto-approves file ops; asks for everything else | Interactive dev workflows |
| `"dontAsk"` | Denies anything not in `allowedTools` | Locked-down headless pipelines |
| `"bypassPermissions"` | Approves everything (except `disallowedTools`) | Fully trusted sandboxed CI |
| `"auto"` (TS only) | Model classifier decides per tool | Autonomous agents with guardrails |
| `"default"` | Falls through to `canUseTool` for every unresolved tool | Custom approval flows |

```python
# Locked-down read-only agent
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Glob", "Grep"],
    permission_mode="dontAsk",              # anything not in allowedTools is denied
    disallowed_tools=["Bash"],              # extra safety: deny even if mode changes
)
```

```python
# Interactive approval
async def ask_user(tool_name, input_data, context):
    print(f"\nClaude wants to use: {tool_name}")
    print(f"Input: {input_data}")
    answer = input("Allow? [y/n] ").strip().lower()
    return {"behavior": "allow"} if answer == "y" else {"behavior": "deny"}

options = ClaudeAgentOptions(
    permission_mode="default",
    can_use_tool=ask_user,
)
```

---

## Recipe: Get Structured Output

**Reference:** `references/Input and output/Get_structured_output_from_agents.md`

### With JSON Schema

```python
schema = {
    "type": "object",
    "properties": {
        "bugs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "file": {"type": "string"},
                    "line": {"type": "number"},
                    "description": {"type": "string"},
                    "severity": {"type": "string", "enum": ["low", "medium", "high"]},
                },
                "required": ["file", "line", "description", "severity"],
            },
        }
    },
    "required": ["bugs"],
}

async for message in query(
    prompt="Find all bugs in this codebase",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Grep", "Glob"],
        output_format={"type": "json_schema", "schema": schema},
    ),
):
    if isinstance(message, ResultMessage) and message.subtype == "success":
        bugs = message.structured_output["bugs"]
        for bug in bugs:
            print(f"{bug['severity'].upper()} {bug['file']}:{bug['line']} — {bug['description']}")
```

### With Pydantic (Python)

```python
from pydantic import BaseModel

class Bug(BaseModel):
    file: str
    line: int
    description: str
    severity: str

class BugReport(BaseModel):
    bugs: list[Bug]

async for message in query(
    prompt="Find all bugs",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Grep", "Glob"],
        output_format=BugReport,          # pass the Pydantic class directly
    ),
):
    if isinstance(message, ResultMessage) and message.subtype == "success":
        report: BugReport = message.structured_output   # fully typed
        for bug in report.bugs:
            print(f"{bug.severity.upper()} {bug.file}:{bug.line}")
```

---

## Recipe: Customize the System Prompt

**Reference:** `references/Customize behavior/Modifying_system_prompts.md`

```python
# Option 1: Fully custom prompt (replaces everything)
options = ClaudeAgentOptions(
    system_prompt="You are a senior Go engineer. Follow idiomatic Go conventions.",
)

# Option 2: Append to the Claude Code preset
options = ClaudeAgentOptions(
    system_prompt={
        "type": "preset",
        "preset": "claude_code",
        "append": "Always write tests for every function you create.",
    }
)

# Option 3: Load CLAUDE.md from the project directory
options = ClaudeAgentOptions(
    system_prompt={"type": "preset", "preset": "claude_code"},
    setting_sources=["project"],   # loads ./CLAUDE.md and ./.claude/CLAUDE.md
)
```

> **Default behavior:** Without specifying `system_prompt`, the SDK uses a minimal prompt (tool instructions only, no Claude Code coding guidelines). Use the `"claude_code"` preset to get the full experience.

---

## Recipe: OpenTelemetry Tracing

**Reference:** `references/Control and observability/Observability_with_OpenTelemetry.md`

The SDK runs the CLI as a child process; the CLI exports OTEL data directly. Configure via environment variables — either in your shell/container or via `options.env`.

```python
options = ClaudeAgentOptions(
    env={
        "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
        "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA": "1",  # required for traces
        "OTEL_TRACES_EXPORTER": "otlp",
        "OTEL_METRICS_EXPORTER": "otlp",
        "OTEL_LOGS_EXPORTER": "otlp",
        "OTEL_EXPORTER_OTLP_PROTOCOL": "http/protobuf",
        "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.example.com:4318",
        "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer your-token",
        "OTEL_SERVICE_NAME": "my-agent",   # distinguishes agents in your backend
    }
)
```

```typescript
options: {
  // In TypeScript, env REPLACES the inherited environment — spread process.env first
  env: {
    ...process.env,
    CLAUDE_CODE_ENABLE_TELEMETRY: "1",
    CLAUDE_CODE_ENHANCED_TELEMETRY_BETA: "1",
    OTEL_TRACES_EXPORTER: "otlp",
    OTEL_METRICS_EXPORTER: "otlp",
    OTEL_LOGS_EXPORTER: "otlp",
    OTEL_EXPORTER_OTLP_PROTOCOL: "http/protobuf",
    OTEL_EXPORTER_OTLP_ENDPOINT: "http://collector.example.com:4318",
    OTEL_SERVICE_NAME: "my-agent",
  }
}
```

**Span names to know:** `claude_code.interaction` (one agent turn) → `claude_code.llm_request` → `claude_code.tool` → `claude_code.tool.execution`. Filter by `session.id` to see all spans for one session.

**Content is not exported by default.** Opt in with: `OTEL_LOG_USER_PROMPTS=1`, `OTEL_LOG_TOOL_DETAILS=1`, `OTEL_LOG_TOOL_CONTENT=1`.

> **Note:** Don't set `console` as an exporter — it conflicts with the SDK's message channel. Use `otlp` pointing at a local Jaeger/collector instead.

---

## Recipe: Rewind File Changes

**Reference:** `references/Control and observability/Rewind_file_changes_with_checkpointing.md`

Checkpointing snapshots files before each Write/Edit turn. You can restore to any snapshot after the fact. Only Write, Edit, and NotebookEdit are tracked — Bash commands are not.

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, UserMessage, ResultMessage

async def main():
    options = ClaudeAgentOptions(
        enable_file_checkpointing=True,
        permission_mode="acceptEdits",
        extra_args={"replay-user-messages": None},  # required to get UUIDs in the stream
    )

    checkpoint_id = None
    session_id = None

    async with ClaudeSDKClient(options) as client:
        await client.query("Refactor the auth module")
        async for msg in client.receive_response():
            if isinstance(msg, UserMessage) and msg.uuid and not checkpoint_id:
                checkpoint_id = msg.uuid          # first UUID = restore-to-original point
            if isinstance(msg, ResultMessage):
                session_id = msg.session_id

    # Later: resume with empty prompt, then rewind
    if checkpoint_id and session_id:
        async with ClaudeSDKClient(
            ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
        ) as client:
            await client.query("")
            async for msg in client.receive_response():
                await client.rewind_files(checkpoint_id)
                break

asyncio.run(main())
```

**Key points:**
- Capture the *first* `UserMessage.uuid` to get a "restore to original" point; capture *all* to build multiple restore points
- You can also rewind mid-stream (before the loop ends) to abort and undo in one step
- Rewinding restores file content only — it does not rewind the conversation history

---

## Recipe: Stream Input Messages

**Reference:** `references/Input and output/Streaming_input.md`

Use an async generator as the `prompt` to send multiple messages, images, or interruptible inputs to the same agent session.

```python
import asyncio, base64
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage
from claude_agent_sdk.types import TextBlock

async def main():
    async def messages():
        yield {"type": "user", "message": {"role": "user", "content": "Analyze this codebase"}}
        await asyncio.sleep(2)   # wait for any condition before sending the next message
        with open("diagram.png", "rb") as f:
            img = base64.b64encode(f.read()).decode()
        yield {
            "type": "user",
            "message": {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Now review this architecture diagram"},
                    {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": img}},
                ],
            },
        }

    async with ClaudeSDKClient(ClaudeAgentOptions(allowed_tools=["Read", "Grep"])) as client:
        await client.query(messages())
        async for msg in client.receive_response():
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock): print(block.text)

asyncio.run(main())
```

**When to use:** image attachments, queued follow-up messages, real-time interruption, or any case where you need to inject input mid-session. For simple one-shot queries, the standard `query(prompt="...")` is sufficient.

---

## Recipe: Scale with Tool Search

**Reference:** `references/Extend with tools/scale_to_many_tools_with_tool_search.md`

With 30+ tools, context fills up and tool selection accuracy drops. Tool search defers loading definitions until needed.

```python
options = ClaudeAgentOptions(
    mcp_servers={
        "enterprise-tools": {"type": "http", "url": "https://tools.example.com/mcp"}
    },
    allowed_tools=["mcp__enterprise-tools__*"],   # wildcard pre-approves all tools
    env={"ENABLE_TOOL_SEARCH": "auto:5"},          # activate when tools > 5% of context
)
```

| `ENABLE_TOOL_SEARCH` value | Behavior |
|---|---|
| (unset) / `true` | Always on — definitions never pre-loaded |
| `auto` | Activates when definitions exceed 10% of context window |
| `auto:N` | Activates at N% threshold |
| `false` | Off — all definitions loaded upfront (fine for <10 tools) |

**Make tools discoverable:** use descriptive names (`search_slack_messages` beats `query_slack`) and add tool category hints to your system prompt: `"You can search for tools to interact with Slack, GitHub, and Jira."`

> Requires Claude Sonnet 4+ or Opus 4+. Not supported on Haiku.

---

## Recipe: Load Skills in the SDK

**Reference:** `references/Customize behavior/Agent_skills_in_the_sdk.md`

Skills are `SKILL.md` files in `.claude/skills/`. The SDK doesn't load them by default — you must opt in.

```python
options = ClaudeAgentOptions(
    cwd="/path/to/project",                    # must contain .claude/skills/
    setting_sources=["user", "project"],       # loads skills from filesystem
    allowed_tools=["Skill", "Read", "Bash"],   # "Skill" tool must be listed
)
```

```typescript
options: {
  cwd: "/path/to/project",
  settingSources: ["user", "project"],
  allowedTools: ["Skill", "Read", "Bash"],
}
```

**Skill locations:**
- Project skills: `.claude/skills/*/SKILL.md` — shared via git
- Personal skills: `~/.claude/skills/*/SKILL.md` — available across all projects

> The `allowed-tools` frontmatter in `SKILL.md` is ignored when running through the SDK. Control tool access via `allowedTools` on the query instead.

---

## Recipe: Track Cost and Usage

**Reference:** `references/Control and observability/Track_cost_and_usage.md`

```python
async for message in query(prompt="...", options=options):
    if isinstance(message, ResultMessage):
        cost = message.total_cost_usd
        print(f"Total cost: ${cost:.4f}")
        if message.usage:
            print(f"Input tokens: {message.usage.input_tokens}")
            print(f"Output tokens: {message.usage.output_tokens}")

# Set a cost cap (agent stops and returns error_max_budget_usd if exceeded)
options = ClaudeAgentOptions(max_cost_usd=0.50)
```

---

## Recipe: Deploy to Production

**Reference:** `references/Deployment/Hosting_the_Agent_SDK.md`, `references/Deployment/Securely_deploying_AI_agents.md`

**Container requirements:**
- Python 3.10+ or Node.js 18+
- Node.js present (SDK spawns the Claude Code CLI internally — it's bundled, no separate install)
- 1 GiB RAM, 5 GiB disk, 1 CPU (scale to task)
- Outbound HTTPS to `api.anthropic.com`

**Recommended sandbox providers:** Modal, E2B, Fly Machines, Vercel Sandbox, Cloudflare Sandboxes

**Production checklist:**
- [ ] Run inside a container with no persistent home directory
- [ ] Set `permission_mode="bypassPermissions"` only inside sandboxed containers
- [ ] Set `disallowed_tools=["Bash"]` if the agent shouldn't run shell commands
- [ ] Set `max_cost_usd` to prevent runaway costs
- [ ] Use `hooks` for audit logging of all file writes
- [ ] Never expose `ANTHROPIC_API_KEY` in agent output or logs

---

## Recipe: Migrate from Old SDK

**Reference:** `references/SDK references/Migrate_to_Claude_Agent_SDK.md`

The package was renamed. Update your imports:

```bash
# Python: remove old, install new
pip uninstall claude-code-sdk && pip install claude-agent-sdk

# TypeScript: remove old, install new
npm uninstall @anthropic-ai/claude-code && npm install @anthropic-ai/claude-agent-sdk
```

```python
# Before
from claude_code_sdk import query, ClaudeCodeOptions

# After
from claude_agent_sdk import query, ClaudeAgentOptions
```

```typescript
// Before
import { query } from "@anthropic-ai/claude-code";

// After
import { query } from "@anthropic-ai/claude-agent-sdk";
```

All option names, message types, and behavior are identical — only the package name and class names changed.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Subagent not being invoked | Include `"Agent"` in parent's `allowed_tools`; write a clearer `description`; or name it explicitly in the prompt |
| `resume` returns a fresh session | `cwd` must match the original session's directory — sessions are stored under `~/.claude/projects/<encoded-cwd>/` |
| `bypassPermissions` + `allowedTools` doesn't restrict tools | `allowedTools` only pre-approves — it doesn't deny unlisted tools. Use `disallowed_tools` or `dontAsk` mode to block |
| Custom tool never called | Tool must be in `mcp_servers` AND `allowed_tools`; tool `description` must make its purpose clear |
| No CLAUDE.md loaded | Set `setting_sources=["project"]` — it is not loaded automatically, even with `preset: "claude_code"` |
| Cost explodes in loops | Set `max_cost_usd` and handle `error_max_budget_usd` in `ResultMessage.subtype` |
| Skills not found in SDK | Need both `setting_sources=["user", "project"]` AND `"Skill"` in `allowed_tools` — either alone is insufficient |
| TypeScript `env` drops API key | In TypeScript, `options.env` *replaces* the inherited environment entirely — always spread `...process.env` first |
| Checkpointing: no UUIDs in stream | Add `extra_args={"replay-user-messages": None}` (Python) or `extraArgs: {"replay-user-messages": null}` (TS) |
| Checkpointing: `rewindFiles` after loop ends | The CLI connection closes when the loop completes — resume with an empty prompt first, then call `rewind_files` |
| Tool selection breaks with many tools | With 30+ tools, set `ENABLE_TOOL_SEARCH=auto` via `env={"ENABLE_TOOL_SEARCH": "auto"}` in `ClaudeAgentOptions` |
| OTEL `console` exporter breaks the SDK | The CLI uses stdout as its message channel — use `otlp` exporter pointing at a local collector instead |

---

## Reference Quick Links

See [INDEX.md](INDEX.md) for the full reference index.

**Most-used references:**
- **API shape:** `references/SDK references/Agent_SDK_reference_Python.md` or `…TypeScript.md`
- **Message types:** `references/Core concepts/How_the_agent_loop_works.md`
- **All options:** `references/SDK references/Agent_SDK_reference_Python.md` → `ClaudeAgentOptions`
