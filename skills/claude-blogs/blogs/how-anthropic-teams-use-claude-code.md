# How Anthropic Teams Use Claude Code

**Source:** https://claude.com/blog/how-anthropic-teams-use-claude-code  
**Published:** July 24, 2025  
**Categories:** Enterprise AI, Claude Code

## Overview

Anthropic employees across departments use Claude Code in surprising ways—from traditional development to entirely new workflows for non-technical teams.

## Codebase Navigation and Understanding

- New team members leverage Claude Code to quickly become productive
- Infrastructure data scientists feed entire codebases to Claude—it reads CLAUDE.md files, explains data pipeline dependencies, identifies upstream sources
- Product Engineering calls Claude Code their "first stop" for programming tasks—identifies which files need examination before building

## Testing and Code Review

- Product Design automates PR comments via GitHub Actions—Claude handles formatting and test refactoring
- Security Engineering uses Claude for test-driven development guidance, resulting in more reliable, testable code
- Translates tests across languages: when Inference teams need Rust tests for unfamiliar logic, Claude writes native Rust

## Debugging and Troubleshooting

- Security Engineering resolves production incidents **3x faster** by feeding Claude stack traces and documentation
- During a Kubernetes outage, Data Infrastructure used Claude to diagnose pod IP address exhaustion from dashboard screenshots—saved ~20 minutes during critical downtime

## Prototyping and Feature Development

- Product Design feeds Figma files to Claude, establishing autonomous loops (write code → run tests → iterate)
- Data scientists without TypeScript fluency build entire React applications for visualizing model performance
- Claude maps error states and logic flows during design, identifying edge cases before development begins

## Documentation and Knowledge Management

- Inference team: reduced research time **80%** (1 hour → 10–20 minutes)
- Security Engineering: ingests multiple documentation sources, creates markdown runbooks and troubleshooting guides

## Automation and Workflow Optimization

- Growth Marketing: agentic workflows processing hundreds of ads in minutes—Figma plugin generates up to 100 ad variations by swapping headlines in half a second
- Legal: prototype "phone tree" systems connecting team members with appropriate lawyers

## Key Insight

The most successful teams treat Claude Code as a **thought partner** rather than a code generator—exploring possibilities, prototyping rapidly, and sharing discoveries across technical and non-technical users.
