# Claude Code and Slack

**Source:** https://claude.com/blog/claude-code-and-slack  
**Published:** December 8, 2025  
**Categories:** Product announcements, Claude Code, Coding

## Overview

Anthropic has launched an integration enabling teams to invoke Claude Code directly from Slack conversations. This beta feature bridges the gap between discussion and implementation.

## Key Capabilities

Mention @Claude in Slack for:
- **Bug fixes**: Claude investigates reported issues and implements solutions
- **Feature implementation**: Quick code modifications based on team feedback
- **Collaborative debugging**: Using context from channel discussions

## How It Works

When @Claude is mentioned in a Slack message, the system evaluates whether the request represents a coding task. For eligible requests, Claude automatically creates a new Code session, pulling relevant context from recent messages in the channel and thread.

The system intelligently selects which repository to use based on repositories previously authenticated in Claude Code. As work progresses, Claude posts status updates back to the originating Slack thread. Upon completion, users receive links to the full session and direct access to open pull requests.

## Getting Started

Requirements:
- Claude Slack app installed from the Slack App Marketplace
- Authenticated Claude account
- Access to Claude Code on the web
