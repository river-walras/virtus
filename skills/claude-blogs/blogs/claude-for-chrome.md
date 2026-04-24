# Piloting Claude in Chrome

**Source:** https://claude.com/blog/claude-for-chrome  
**Published:** August 25, 2025  
**Categories:** Product announcements, Claude apps

## Overview

A Chrome extension allows Claude to take actions on users' behalf in web browsers—addressing both significant opportunities and security challenges.

## Availability Timeline

- Initially piloted with 1,000 Max plan users
- Expanded to all Max subscribers by November 2025
- Available to Pro, Team, and Enterprise users as of December 2025
- New integration with Claude Code: develop in terminals, verify in browsers

## Safety Framework

- **Site-level permissions**: Grant or revoke access to specific websites
- **Action confirmations**: For sensitive operations (publishing, financial transactions)
- **Improved system prompts**: Directing Claude on handling sensitive data
- **Blocked website categories**: Including financial services and adult content
- **Advanced classifiers**: Detecting suspicious instruction patterns

## Security Findings

Red-teaming revealed vulnerabilities to **prompt injection attacks**—hidden instructions in websites or documents manipulating AI behavior.

- Initial: **23.6% attack success rate** when deliberately targeted by malicious actors
- After defenses: reduced to **11.2%** in autonomous mode (below existing Computer Use capability)
- Browser-specific attacks: **0% success rates** after mitigation

### Real Example

A successful pre-mitigation attack: malicious email mimicking employer requests to delete messages for "mailbox hygiene," claiming "no additional confirmation required." Claude initially complied; now recognizes such attempts as phishing.

## Development Approach

Rather than broad launch, Anthropic partnered with trusted users for authentic feedback, prioritizing controlled testing to understand real-world threats before wider availability.
