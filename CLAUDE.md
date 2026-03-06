# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a curated "awesome list" — a Markdown-only repository with no build system, dependencies, or tests. All content lives in `README.md`.

## Contributing

Changes consist solely of editing `README.md` to add, update, or remove entries. The list is organized into sections:

- **Tools** — Code assistants, IDEs, Frameworks/Libs
- **Books** — (currently empty, marked `???`)
- **Blog Posts** — Written articles and videos
- **Utils** — Useful references and methodologies
- **Concepts** — Definitions of AI/LLM-related terms (mostly empty, marked `???`)
- **Mentors** — (referenced in TOC but not yet present)

Entries marked `???` are placeholders awaiting content contributions.

## Format Conventions

- Section headers use `##` and `###`
- Each entry is a Markdown link: `- [Name](URL)`
- The Table of Contents uses checkboxes (`- [x]`) linked to section anchors
- License badge is an image link at the bottom (`MIT.png`)

## Skills

- [Claude Code Skills](https://code.claude.com/docs/pt/skills)
- [Agent Skills](https://agentskills.io/home)

## MCP

| MCP                | Descrição                                                                    | Link                                   | ...         |
| ------------------ | ---------------------------------------------------------------------------- | -------------------------------------- | ----------- |
| Grafana MCP server | This provides access to your Grafana instance and the surrounding ecosystem. | https://github.com/grafana/mcp-grafana | :hourglass: |

### MCP Installation

```bash
claude mcp add --transport sse atlasian https://mcp.atlassian.com/v1/sse -s user
claude mcp add --transport http gh https://api.githubcopilot.com/mcp -H "Authorization: Bearer <GITHUB_TOKEN>"
claude mcp add --transport http datadog-mcp https://mcp.us5.datadoghq.com/api/unstable/mcp-server/mcp
```
