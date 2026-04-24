# Audit Claude Platform Activity with the Compliance API

**Source:** https://claude.com/blog/claude-platform-compliance-api  
**Published:** March 30, 2026  
**Categories:** Product announcements, Claude Platform

## Overview

The Compliance API is now available on the Claude Platform, providing administrators with programmatic access to audit logs across their organization. This enables security and compliance teams to track user activity, monitor configuration changes, and integrate Claude usage data into existing compliance infrastructure.

## Activity Categories

The API currently tracks two categories:

- **Admin and system activities:** Resource access modifications including adding workspace members, creating API keys, updating account settings, and modifying entity access
- **Resource activities:** User-driven actions creating or modifying resource data, such as file creation, file downloads, or skill deletion

The API logs user login and logout events, account setting updates, and organizational changes but excludes inference activities and direct model interactions.

## Getting Started

Contact your account team to enable the Compliance API for your organization. Once activated, create an admin API key to query the activity feed endpoint. Logging begins after activation; historical data preceding enablement remains unavailable.

Organizations already using the Compliance API for Claude Enterprise can add their Claude API organization to the same parent organization, filtering activity across both from a unified feed.
