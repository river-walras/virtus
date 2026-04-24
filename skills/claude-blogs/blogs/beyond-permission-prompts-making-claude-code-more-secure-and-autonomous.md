# Beyond Permission Prompts: Making Claude Code More Secure and Autonomous

**Source:** https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous  
**Published:** October 8, 2025  
**Categories:** Claude Code, Product

## Overview

Claude Code's permission-based model creates "approval fatigue." Sandboxing introduces pre-defined boundaries where Claude can operate more freely without constant permission requests—while defending against prompt injection attacks.

## Current Security Model

Claude Code is read-only by default and requests approval before modifying files or executing commands. Static analysis auto-allows safe operations (e.g., `echo`, `cat`), but most actions require explicit user approval.

## Sandboxing Approach

Two critical components:
- **Filesystem Isolation**: Claude can only access/modify specific directories, preventing compromised instances from altering sensitive system files
- **Network Isolation**: Claude connects only to approved servers, blocking data exfiltration or malware downloads

## Two New Features

### Sandboxed Bash Tool (Research Preview)

Developers define which directories and network hosts their agents can access. Built on OS-level primitives (Linux bubblewrap, macOS seatbelt), enforcing restrictions at the OS level—covering direct interactions and spawned subprocesses.

- Permits read/write to current working directory; blocks external file modifications
- Network access routes through a proxy enforcing domain restrictions, with user confirmation for new requests

Activate with: `claude --sandbox`

### Claude Code on the Web

Cloud-based offering executing each session in an isolated sandbox with full server access. Sensitive credentials (git credentials, signing keys) never enter the sandbox environment. A custom proxy handles all git interactions transparently with scoped credentials.

Available at claude.com/code.

## For Developers

Developers building custom agents can leverage the open-sourced sandboxing code.
