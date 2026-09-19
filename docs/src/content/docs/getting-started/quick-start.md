---
title: Quick Start
description: Information about getting started.
---

This guide walks through creating your first project using Create Python App.

## Start the Wizard

Run:

```bash
create-python-app
```

The setup wizard will guide you through the project creation process.

## Project Name

Choose a name for your project.

Example:

```text
❯ What is your project name? my-python-app
```

The project name will be used when creating folders and project metadata.

## Project Location

Choose where the project should be created.

Example:

```text
❯ Where should we create this project? C:\Projects\my-python-app
```

If the specified directory does not already exist, Create Python App will create it automatically.

## Editor Selection

Choose the editor you intend to use.

Example:

```text
❯ Choose your editor: VSCode
```

Supported editors currently include:

- VSCode
- Cursor
- Vim
- Other

## Plugin Selection

If supported by the selected editor, optional plugins can be chosen.

Example:

```text
❯ Select packages: Python Extension (VSCode), Pylance
```

## Review Configuration

Before creating the project, Create Python App displays a summary of the selected options.

Example:

```text
Project: my-python-app
Location: C:\Projects\my-python-app
Editor: VSCode
Plugins: Python Extension (VSCode), Pylance
```

Confirm the configuration to continue.

## Project Creation

Create Python App will:

- Create a virtual environment.
- Create a standard project structure.
- Generate starter files.
- Save project metadata.
- Configure editor-specific settings where applicable.

## Example Project Structure

```text
my-python-app/
├── pyproject.toml
├── README.md
├── src/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_sample.py
└── docs/
    └── README.md
```

## Next Steps

Once project creation is complete:

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run the sample application:

```bash
python src/app.py
```

If using VS Code:

```bash
code .
```

## Learn More

After creating your first project, explore:

- Installation
- Project Structure
- VS Code Support
- Wizard Reference