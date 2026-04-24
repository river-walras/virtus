# Bringing Automated Preview, Review, and Merge to Claude Code on Desktop

**Source:** https://claude.com/blog/preview-review-and-merge-with-claude-code  
**Published:** February 20, 2026  
**Categories:** Claude Code, Coding

## Overview

Claude Code on desktop has received significant updates enabling developers to complete the full development workflow without switching between tools.

## Key Features

### Live App Preview
Developers can now start development servers directly within Claude Code's desktop interface. The system displays the running web application, monitors console logs, catches errors, and iterates automatically. Users can select visual elements in the preview to provide direct feedback.

### Automated Code Review
A new "Review code" button allows Claude to examine local code differences and provide inline commentary. Reviews highlight potential bugs, offer suggestions, and identify issues directly in the diff viewer.

### PR Monitoring and Auto-Fix
For GitHub-hosted repositories, Claude Code monitors pull request status using the GitHub CLI. The system tracks CI check results and can automatically attempt to fix failures. An optional auto-merge feature enables automatic merging once all checks pass.

### Cross-Platform Session Continuity
Sessions now sync across devices. Users can transition from CLI to desktop using the `/desktop` command, or move local sessions to the cloud and continue on mobile or web browsers.

## Availability

Available immediately to all users. Update or download Claude Code on desktop to access the new capabilities.
