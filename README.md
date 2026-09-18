# create-python-app

A guided command-line wizard for creating new Python projects in minutes.

create-python-app is a guided command-line wizard that creates a project structure, configures your development environment, creates a virtual environment, and helps you start coding quickly with sensible defaults.


## Why create-python-app?

Starting a new Python project often means repeating the same setup steps:

- Creating a project structure
- Creating and configuring a virtual environment
- Choosing and configuring an editor
- Installing recommended tooling and extensions
- Setting up a solid foundation before writing any code

While there are many excellent project generators available, create-python-app takes a deliberately simple approach.

The goal isn't to generate every possible type of application, framework, or architecture. Instead, it focuses on helping developers get from:

> "I have an idea."

to

> "I'm writing code."

as quickly as possible.

create-python-app provides a guided setup experience with sensible defaults, editor-aware configuration, and a workflow designed to help you start building immediately.

### Design Principles

create-python-app is built around a few simple ideas:

- **Simple by default** - sensible defaults should require minimal configuration.
- **Guided, not overwhelming** - users should not need to understand dozens of options before getting started.
- **Editor-aware** - the setup experience should adapt to the tools you use.
- **Beginner-friendly** - useful for developers of all experience levels.
- **Practical foundations** - start with a clean project structure and modern development practices.
- **Focused on productivity** - spend less time configuring and more time building.

The aim is simple:

> Ask a few questions, create a solid foundation, and get out of your way.


## Features

✅ Guided setup wizard

✅ Automatic virtual environment creation

✅ Optional editor extension installation

✅ Support for VS Code, Cursor, PyCharm and Vim

✅ Beginner-friendly defaults

✅ Clear next-step guidance after project creation



## Screenshot

![Example output for creating a site](images/happy-path.png)



## Installation

### PyPI

```bash
pip install create-python-app
```

### pipx

```bash
pipx install create-python-app
```

---

## Quick Start

Create a new project:

```bash
create-python-app
```

The wizard will guide you through:

- Choosing a project name
- Selecting a project location
- Choosing an editor
- Installing optional extensions
- Creating a virtual environment

---

## Example

```text
❯ What is your project name?
my-python-app

❯ Where should we create this project?
C:\Projects\my-python-app

❯ Choose your editor
VS Code

❯ Select any plugins to install
✓ Python Extension (VSCode)
✓ Pylance
```

Result:

```text
my-python-app/
│
├── .venv/
├── src/
├── tests/
├── README.md
└── pyproject.toml
```

---

## Supported Editors

- VS Code
- Cursor
- PyCharm
- Vim
- Other

---

## Documentation

Full documentation is available at:

https://create-python-app.dev

---

## Roadmap

See:

ROADMAP.md

for upcoming features and planned improvements.

---

## Contributing

Contributions, bug reports and feature requests are welcome.

Please open an issue or discussion on GitHub.

---

## License

MIT License

See `LICENSE` for details.