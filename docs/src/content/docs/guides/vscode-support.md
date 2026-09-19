---
title: VSCode Support
description: Information about support for VSCode.
---

Create Python App provides support for Microsoft Visual Studio Code during project creation.

The goal is to reduce the amount of manual setup required when starting a new Python project.

## Automatic Detection

During setup, Create Python App attempts to detect whether VS Code is available on the system.

If detected, VS Code is offered as the default editor during the setup process.

Example:

```text
❯ Choose your editor: VSCode
```

## Extension Installation

When VS Code is selected, Create Python App can install optional extensions.

Examples include:

- Python Extension (VSCode)
- Pylance
- Jupyter

During setup:

```text
❯ Select packages: Python Extension (VSCode), Pylance
```

Selected extensions are installed automatically where possible.

## Project Configuration

Create Python App can generate a VS Code configuration folder:

```text
.vscode/
```

including:

```text
.vscode/settings.json
```

This helps ensure that VS Code uses the correct Python interpreter for the project.

## Virtual Environment Support

When a virtual environment is created, Create Python App configures VS Code to use that environment as the project's Python interpreter.

This helps ensure:

- Correct dependency resolution
- Correct linting and formatting
- Consistent behaviour across terminals and editors

## Opening the Project

After project creation is complete, Create Python App displays a suggested command for opening the project:

```bash
code .
```

Running this command from inside the project directory opens the project directly in VS Code.

## Current Scope

Create Python App currently provides:

- VS Code detection
- Extension installation
- Project-specific settings generation
- Virtual environment configuration
- Quick-start commands

## Future Plans

Future releases may include:

- Enhanced VS Code configuration
- Additional extension support
- Deeper editor integration
- A dedicated VS Code extension