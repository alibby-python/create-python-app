---
title: Contributing
description: Information for contributors.
---

Thank you for your interest in contributing to Create Python App.

Contributions of all sizes are welcome. Before creating commits, issues or pull requests, please review the guidelines below.

## Development Guidelines

When contributing to Create Python App:

- Keep changes focused and atomic where practical.
- Ensure all automated tests pass before committing.
- Ensure Ruff checks and formatting checks pass.
- Add or update tests when modifying functionality.
- Update documentation when introducing user-facing changes.
- Follow the Conventional Commit conventions described below.
- Discuss large or architectural changes before implementation.


## Commit Guidelines

Where possible:

- Keep commits focused on a single logical change.
- Avoid mixing features, refactoring and formatting changes in the same commit.
- Use clear Conventional Commit messages.
- Write commit messages in the imperative style (for example, `feat: add plugin support` rather than `feat: added plugin support`).

## Conventional Commits

Create Python App uses Conventional Commits. Please use one of the following formats when structuring commit messages.

### Features

`feat: add plugin support`

Introduces new functionality in a backwards-compatible way.

**Version impact:** Minor release (`0.1.0 → 0.2.0`).

### Bug Fixes

`fix: correct project path validation`

Corrects defects, bugs or unintended behaviour.

**Version impact:** Patch release (`0.1.0 → 0.1.1`).

### Documentation

`docs: update installation guide`

Updates project documentation without changing application behaviour.

**Version impact:** No version change by default.

### Tests

`test: improve prompt coverage`

Adds or updates automated tests without changing application functionality.

**Version impact:** No version change by default.

### Build

`build: consolidate dependencies into pyproject.toml`

Changes packaging, dependency management, build tooling or release configuration.

**Version impact:** No version change by default.

### Continuous Integration

`ci: configure Dependabot updates`

Changes GitHub Actions, CI pipelines or automation workflows.

**Version impact:** No version change by default.

### Style

`style: apply Ruff formatting`

Formatting, whitespace or code-style changes that do not alter behaviour.

**Version impact:** No version change by default.

### Refactoring

`refactor: simplify keyboard handling`

Improves internal code structure without changing functionality.

**Version impact:** No version change by default.

### Breaking Changes

`feat!: redesign plugin configuration`

`BREAKING CHANGE: Plugin configuration format has changed.`

Introduces a backwards-incompatible change that requires users to modify existing code, configuration or behaviour.

**Version impact:** Major release (`1.0.0 → 2.0.0`).