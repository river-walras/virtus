# Automate Security Reviews with Claude Code

**Source:** https://claude.com/blog/automate-security-reviews-with-claude-code  
**Published:** August 6, 2025  
**Categories:** Product announcements, Claude Code

## Overview

Claude Code now includes automated security review capabilities—a `/security-review` command and GitHub Actions integration to identify and fix vulnerabilities before code reaches production.

## Terminal-Based Security Analysis

The `/security-review` command performs ad-hoc security assessments directly from the terminal, checking for:
- SQL injection risks
- Cross-site scripting
- Authentication flaws
- Insecure data handling
- Dependency vulnerabilities

Once vulnerabilities are identified, developers can request Claude Code to implement fixes immediately within their development workflow.

## Automated Pull Request Reviews

A GitHub Action automates security analysis for every pull request:
- Automatically triggers upon PR creation
- Reviews code changes for security concerns
- Filters customizable rules to reduce false positives
- Posts inline comments with vulnerability findings and fix recommendations

## Real-World Implementation at Anthropic

Used internally:
- Detected a remote code execution vulnerability through DNS rebinding in a local HTTP server
- Identified SSRF attack vulnerabilities in a credential management proxy

Both flagged before merging.

## Getting Started

- `/security-review` command: Update to latest Claude Code version
- GitHub Action: Configure via documentation on the `anthropics/claude-code-security-review` repository

Available to all Claude Code users.
