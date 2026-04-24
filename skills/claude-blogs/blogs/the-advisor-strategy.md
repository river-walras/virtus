# The advisor strategy: Give agents an intelligence boost

**Source:** https://claude.com/blog/the-advisor-strategy  
**Published:** April 9, 2026  
**Categories:** Product announcements, Claude Platform, Agents

## Overview

Developers seeking to balance intelligence with cost have adopted the "advisor strategy": pairing Opus as an advisor with Sonnet or Haiku as an executor. This approach delivers near Opus-level reasoning while maintaining costs close to Sonnet levels.

Anthropic is launching the advisor tool on the Claude Platform to streamline this pattern into a single API modification.

## How the Advisor Strategy Works

In this architecture, Sonnet or Haiku operates as the executor, managing tasks end-to-end by calling tools, processing results, and iterating toward solutions. When facing decisions beyond its capability, the executor consults Opus for guidance. Opus accesses shared context and provides direction—whether a plan, correction, or stop signal—then the executor resumes. Crucially, the advisor never invokes tools or generates user-facing output; it only provides guidance.

This inverts traditional sub-agent patterns where larger models orchestrate and delegate work. Here, the smaller, cost-effective model drives execution and escalates only when necessary.

## Performance and Cost Metrics

- Sonnet with Opus advisor: **2.7 percentage point increase on SWE-bench Multilingual** over Sonnet alone, while **reducing cost per agentic task by 11.9%**
- Haiku with Opus advisory scored **41.2% on BrowseComp**—more than double its solo 19.7% performance, at **85% lower cost per task** than standalone Sonnet

## API Implementation

```python
response = client.messages.create(
    model="claude-sonnet-4-6",  # executor
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6",
            "max_uses": 3,
        },
        # ... your other tools
    ],
    messages=[...]
)
```

The executor model determines when to invoke the advisor. Context routing, advisory response generation, and executor continuation all occur within a single request—no extra round-trips required. Advisor tokens are reported separately in usage data.

## Key Features

- **Billing**: Advisor tokens charged at advisor model's rates; executor tokens at executor's rates
- **Cost Controls**: `max_uses` parameter caps advisor invocations per request
- **Tool Compatibility**: The advisor tool coexists with existing tools
