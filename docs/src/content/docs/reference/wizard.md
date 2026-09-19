---
title: Wizard Reference
description: Reference documentation for Create Python App wizard steps.
generated: true
version: 0.1.0
lastUpdated: 2026-09-18
tags:
  - wizard
  - reference
sidebar:
  order: 10
---

This page is generated automatically from source code documentation.


## Step 1: Project Name

### Description

The name of your new Python project; this will also
form the base of the virtual environment.

### Type

`string`

### Default

`my-python-app`

### Example

`my-cool-app`

## Step 2: Project Dir

### Description

Where the new project should be created.
Defaults to the root of the current drive plus the
project name.

### Type

`string`

### Default

`C:\\my-python-app`

### Example

`C:\\Projects\\my-cool-app`

## Step 3: Editor

### Description

Choose your preferred editor for this project.
VSCode is auto-detected if available.

### Type

`string`

### Options

- `VSCode`
- `PyCharm`
- `Vim`
- `Other`

### Example

`VSCode`

## Step 4: Plugins

### Description

Pick optional editor extensions to install.
Currently available when VSCode is selected.

### Type

`array[string]`

### Example

- `Pylance`
- `Jupyter`

## Step 5: Confirmation

### Description

Displays a summary of the selected options and
requests confirmation before project generation
begins.

### Type

`boolean`

### Default

`true`

### Example

`Yes`

## Step 6: Create Virtual Environment

### Description

Creates a Python virtual environment for the
new project.

### Type

`operation`

## Step 7: Create Project Folders

### Description

Creates the standard project directory structure,
including source code, tests, and documentation
folders.

### Type

`operation`

## Step 8: Create Project Files

### Description

Creates the initial project files required for
development.

### Type

`operation`

## Step 9: Vscode Plugins

### Description

Installs selected VSCode extensions
automatically.

### Type

`array[string]`

### Example

- `Pylance`
- `Python Debugger`

## Step 10: Save Metadata

### Description

Saves the selected configuration options
to a JSON file for future reference.

### Type

`object`

### Fields

| Field | Description |
|-------|-------------|
| `project_name` | |
| `project_path` | |
| `editor` | |
| `plugins` | |
| `venv_path` | |

## Step 11: Setup Summary

### Description

Displays a final summary of the completed
project configuration.

### Type

`object`

### Fields

| Field | Description |
|-------|-------------|
| `project_name` | |
| `project_path` | |
| `editor` | |
| `plugins` | |
| `venv_path` | |

## Step 12: Next Steps

### Description

Displays guidance on activating the virtual
environment, opening the project, and
beginning development.

### Type

`object`

### Fields

| Field | Description |
|-------|-------------|
| `project_path` | |
| `venv_path` | |
| `editor` | |
