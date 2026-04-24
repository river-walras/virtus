# Introduction to agentic coding

**Source:** https://claude.com/blog/introduction-to-agentic-coding  
**Published:** October 30, 2025  
**Categories:** Claude Code, Coding

## What is Agentic Coding?

Agentic coding represents a fundamental shift from autocomplete assistance to autonomous task execution. Traditional coding assistants suggest next-line completions within single files. Agentic systems:
- Accept high-level goals
- Break them into discrete steps
- Execute those steps independently
- Adjust based on environmental feedback

## Evolution of AI Coding Tools

1. **Code Prediction**: Autocomplete within constrained context windows
2. **Conversational AI**: Chat interfaces for code problems, limited to pasted snippets
3. **Agentic Coding**: Full project-level understanding and autonomous execution

## How Agentic Coding Works

**Context Gathering**: Analyze configuration files, review test patterns, trace import dependencies. Create an adaptive plan that evolves as information emerges.

**Implementation**: Read and write across your codebase, modify multiple related files while maintaining consistency. Adding authentication means updating route handlers, middleware, schemas, API clients, documentation, and tests—all consistently.

## Claude Code in Practice

Operates directly in project directories with full codebase access via the terminal.

```bash
npm install -g @anthropic-ai/claude-code
claude
```

**Multi-file operations**: Requesting "refactor callback-based code to use async/await" triggers identification, updating, error handling changes, test modifications, and test suite verification.

**Permission model**: Claude Code requests approval before modifying files and displays planned changes explicitly.

## Real-World Example: Rakuten

Challenged Claude Code with implementing activation vector extraction in vLLM (12.5M lines across Python, C++, CUDA). Results:
- 79% faster feature delivery (24 days → 5 days)
- 7-hour autonomous implementations with minimal intervention
- 99.9% accuracy on complex algorithmic refactoring
- 5x parallel task execution capacity

## Getting Started

Start with: understanding architecture, analyzing code quality, debugging and fixing, and test automation for uncovered code paths.
