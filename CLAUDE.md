# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the official Anthropic Skills repository - a collection of example skills that extend Claude's capabilities for specialized tasks. Skills are folders containing instructions, scripts, and resources that Claude loads dynamically to perform better at specific tasks.

The repository contains two main categories:
- **document-skills/** - Production skills for document processing (DOCX, PDF, PPTX, XLSX) - source-available reference examples
- **example-skills/** - Open source example skills demonstrating creative, technical, and enterprise capabilities

## Repository Structure

```
skills/
├── .claude-plugin/         # Plugin marketplace configuration
│   └── marketplace.json    # Defines plugin bundles and their included skills
├── agent_skills_spec.md    # Official specification for skill structure
├── document-skills/        # Source-available document processing skills
│   ├── docx/              # Word document creation and editing
│   ├── pdf/               # PDF manipulation toolkit
│   ├── pptx/              # PowerPoint presentation generation
│   └── xlsx/              # Excel spreadsheet processing
├── skill-creator/          # Meta-skill for creating new skills
│   ├── scripts/
│   │   ├── init_skill.py      # Initialize new skill from template
│   │   ├── package_skill.py   # Package skill into .skill file
│   │   └── quick_validate.py  # Validate skill structure
│   └── references/
│       ├── workflows.md       # Patterns for sequential workflows
│       └── output-patterns.md # Patterns for template and quality standards
└── [other-skills]/        # Various example skills
```

## Skill Specification

Every skill must contain a `SKILL.md` file with:

### Required YAML Frontmatter
```yaml
---
name: skill-name              # Lowercase, hyphens only, must match directory name
description: Complete description of what the skill does and when to use it
---
```

### Optional Frontmatter Fields
- `license` - License name or reference to bundled license file
- `allowed-tools` - Pre-approved tools (Claude Code only)
- `metadata` - Custom key-value pairs for client extensions

### Optional Bundled Resources
- `scripts/` - Executable code (Python/Bash) for deterministic operations
- `references/` - Documentation loaded into context as needed
- `assets/` - Templates, images, fonts used in skill output

## Common Development Tasks

### Creating a New Skill

1. **Initialize skill structure:**
   ```bash
   python skill-creator/scripts/init_skill.py <skill-name> --path .
   ```
   This creates a new skill directory with proper YAML frontmatter and example resource folders.

2. **Edit the skill:**
   - Update YAML frontmatter in `SKILL.md` with proper `name` and `description`
   - Write instructions in the Markdown body
   - Add scripts, references, or assets as needed
   - Delete unused example files

3. **Validate skill:**
   ```bash
   python skill-creator/scripts/quick_validate.py <path/to/skill-folder>
   ```

4. **Package for distribution:**
   ```bash
   python skill-creator/scripts/package_skill.py <path/to/skill-folder> [output-dir]
   ```
   Creates a `.skill` file (zip format) that can be distributed and uploaded.

### Testing Skills

Skills can be tested in three ways:
1. **Claude Code:** Install via `/plugin install` after adding to marketplace
2. **Claude.ai:** Upload the .skill file directly (paid plans only)
3. **Claude API:** Use Skills API for programmatic testing

### Validation

Before packaging, validation checks:
- YAML frontmatter format and required fields
- Skill naming conventions match directory name
- Description completeness and quality
- File organization and resource references

## Architecture Principles

### Progressive Disclosure
Skills use a three-level loading system:
1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - Loaded when skill triggers (<5k words, prefer <500 lines)
3. **Bundled resources** - Loaded as needed by Claude

### Context Efficiency
- Keep SKILL.md concise - Claude is already smart, only add what it doesn't know
- Split large skills: use `references/` for detailed docs, keep SKILL.md lean
- Avoid deeply nested references - keep one level deep from SKILL.md
- Use grep patterns in SKILL.md for large reference files (>10k words)

### Degrees of Freedom
- **High freedom (text):** Multiple valid approaches, context-dependent decisions
- **Medium freedom (pseudocode with parameters):** Preferred pattern exists, some variation acceptable
- **Low freedom (specific scripts):** Fragile operations, consistency critical

## Plugin Marketplace Configuration

The `.claude-plugin/marketplace.json` defines two plugin bundles:

1. **document-skills** - DOCX, PDF, PPTX, XLSX
2. **example-skills** - All other skills in repository

To add a new skill to a bundle, update the `skills` array in `marketplace.json`.

## Skill Design Patterns

Consult these resources when creating skills:
- `skill-creator/references/workflows.md` - Sequential workflows and conditional logic
- `skill-creator/references/output-patterns.md` - Template and example patterns
- `agent_skills_spec.md` - Official specification

Common structures:
- **Workflow-Based:** Step-by-step procedures (e.g., document processing)
- **Task-Based:** Different operations/capabilities (e.g., PDF toolkit)
- **Reference/Guidelines:** Standards or specifications (e.g., brand guidelines)
- **Capabilities-Based:** Integrated system features (e.g., product management)

## Important Notes

- **Document skills** are point-in-time snapshots, not actively maintained - use as reference only
- **Example skills** are demonstrations, not production implementations
- Always test skills thoroughly before relying on them for critical tasks
- Skill descriptions are crucial - they determine when the skill triggers
- Keep skills focused on non-obvious procedural knowledge Claude needs
