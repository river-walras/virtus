# Preparing your security program for AI-accelerated offense

**Source:** https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense  
**Published:** April 10, 2026  
**Categories:** Agents, Claude Enterprise, Security

## Overview

Anthropic's security teams have published recommendations for organizations preparing defenses against AI-enabled cyber threats. The guidance stems from Project Glasswing, an initiative using Claude Mythos Preview's cybersecurity capabilities for defensive purposes.

The core concern: AI models are dramatically reducing the time, resources, and expertise required to discover and exploit vulnerabilities. As these capabilities become widely available within 24 months, organizations must fundamentally accelerate their security practices.

## Seven Priority Areas

### 1. Close Your Patch Gap

AI excels at reverse-engineering patches into working exploits. The window between patch publication and exploit availability is shrinking.

**Key actions:**
- Patch all vulnerabilities on the CISA Known Exploited Vulnerabilities catalog immediately
- Use EPSS (Exploit Prediction Scoring System) to prioritize remaining CVEs
- Target 24-hour patching for internet-exposed systems
- Automate patch deployment where feasible

### 2. Handle Higher Vulnerability Volumes

Expect order-of-magnitude increases in vulnerability discovery over the next two years.

**Key actions:**
- Transition from spreadsheet-based tracking to automated systems
- Evaluate open-source dependencies using OpenSSF Scorecard
- Apply security expectations to third-party vendors
- Implement AI-assisted triage to deduplicate findings and estimate exposure

### 3. Find Bugs Before Shipping

Prevention outweighs remediation.

**Key actions:**
- Add static analysis and AI code review to CI/CD pipelines
- Implement automated penetration testing in continuous delivery
- Secure build pipelines using frameworks like SLSA
- Adopt memory-safe languages (Rust, Go) for new development
- Run AI vulnerability scanning on your own code before attackers do

### 4. Scan Existing Codebases

Production code often contains previously-overlooked vulnerabilities that frontier models can identify.

**Key actions:**
- Prioritize internet-facing, input-parsing, and authentication code
- Include legacy systems with minimal recent review
- Budget engineering time for remediation
- Start with one service to establish cost baselines

### 5. Design for Breach

Assume attackers will gain footholds. Limit their reach.

**Key actions:**
- Adopt zero-trust architecture; authenticate every inter-service request
- Tie access to verified hardware rather than credentials alone
- Isolate services by cryptographic identity
- Replace long-lived secrets with short-lived tokens

### 6. Reduce Exposed Surface

Attackers can discover systems you don't know about.

**Key actions:**
- Maintain current inventory of internet-facing hosts and APIs
- Decommission unused legacy systems
- Minimize each service's exposed functionality
- Run autonomous external red-teaming against your own perimeter

### 7. Shorten Incident Response

Response processes taking days are incompatible with rapid exploit timelines.

**Key actions:**
- Deploy AI triage agents for first-pass alert investigation
- Prioritize dwell time reduction and monitoring coverage
- Automate evidence collection and postmortem drafting
- Run tabletop exercises for five simultaneous incidents
- Map detection coverage to MITRE ATT&CK framework

## Vulnerability Reporting Standards

When reporting findings upstream, quality matters. Low-quality automated reports damage maintainer trust.

**Standards for reports:**
- Clear plain-language explanation of the bug and impact
- Detailed code path walkthrough with reproduction steps
- Proposed patch demonstrating understanding of conventions
- Upfront disclosure of AI involvement
- Deference to maintainer judgment

## For Small Organizations

Without dedicated security teams, focus on highest-impact actions:
- Enable automatic updates across all systems
- Prefer managed services over self-hosting
- Use passkeys or hardware security keys
- Enable free code-hosting security tooling (GitHub Dependabot, CodeQL)
- Publish a `SECURITY.md` file for open-source projects
