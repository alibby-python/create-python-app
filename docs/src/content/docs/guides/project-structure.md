---
title: Project Structure
description: Information about the project structure.
---

Create Python App generates a simple, practical project structure designed to help you start development immediately.

A typical generated project looks like:

```text
my-python-app/
├── .venv/
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

## Root Directory

The root directory contains the main project configuration and documentation files.

### `pyproject.toml`

Contains project metadata and Python package configuration.

Example:

```toml
[project]
name = "my-python-app"
version = "0.1.0"
requires-python = ">=3.10"

dependencies = []
```

### `README.md`

The primary documentation file for your project.

Use this to:

- Describe the project.
- Explain installation and usage.
- Document development workflows.

---

## Virtual Environment

### `.venv`

Create Python App automatically creates a Python virtual environment for the project.

The virtual environment helps isolate project dependencies from other Python projects installed on the system.

Typical activation command on Windows:

```bash
.venv\Scripts\activate
```

---

## Source Code

### `src`

The `src` directory contains the application's Python source code.

Example:

```text
src/
├── __init__.py
└── app.py
```

### `app.py`

A simple starter application is generated automatically.

Example:

```python
def main():
    print("Hello from your new Python app!")


if __name__ == "__main__":
    main()
```

---

## Testing

### `tests`

The `tests` directory contains automated tests.

Example:

```text
tests/
└── test_sample.py
```

A sample test is included to help you get started with automated testing.

---

## Documentation

### `docs`

The `docs` directory contains project-specific documentation.

Example:

```text
docs/
└── README.md
```

Use this directory for:

- User guides
- Technical documentation
- Architecture notes
- Development references

---

## Why This Structure?

The generated structure follows a simple principle:

> Keep project files organised, predictable and easy to understand.

The goal is to provide a sensible starting point while remaining flexible enough for projects of any size.

## Next Steps

After project creation:

1. Activate the virtual environment.
2. Open the project in your preferred editor.
3. Begin development in `src/app.py`.
4. Add tests to the `tests` directory.
5. Expand the documentation as the project grows.