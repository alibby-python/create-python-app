#!/usr/bin/env python3

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import tomllib

PROJECT_ROOT = Path(__file__).parent.parent

SOURCE_FILE = PROJECT_ROOT / "create_python_app" / "cli.py"

OUTPUT_FILE = (
    PROJECT_ROOT / "docs" / "src" / "content" / "docs" / "reference" / "wizard.md"
)


SECTION_NAMES = {
    "Wizard Step",
    "Description",
    "Type",
    "Default",
    "Options",
    "Fields",
    "Folders",
    "Files",
    "Result",
    "Example",
}


def get_version() -> str:
    """
    Read the application version from pyproject.toml.
    """

    pyproject = PROJECT_ROOT / "pyproject.toml"

    with open(pyproject, "rb") as f:
        data = tomllib.load(f)

    return data["project"]["version"]


def extract_wizard_docstrings(source: str) -> list[dict]:
    """
    Extract all wizard-step docstrings from the source file.
    """

    matches = re.findall(
        r'"""\s*(.*?)\s*"""',
        source,
        re.DOTALL,
    )

    steps = []

    for docstring in matches:
        if "Wizard Step:" not in docstring:
            continue

        step = parse_docstring(docstring)

        if step:
            steps.append(step)

    return steps


def parse_docstring(docstring: str) -> dict:
    """
    Convert a wizard-step docstring into a dictionary.
    """

    result = {}

    current_section = None

    for line in docstring.splitlines():
        stripped = line.strip()

        if not stripped:
            continue

        matched = False

        for section in SECTION_NAMES:
            prefix = f"{section}:"

            if stripped.startswith(prefix):
                current_section = section

                value = stripped[len(prefix) :].strip()

                result[section] = value

                matched = True
                break

        if matched:
            continue

        if current_section:
            existing = result.get(current_section, "")

            if existing:
                result[current_section] = existing + "\n" + stripped
            else:
                result[current_section] = stripped

    return result


def build_markdown(
    steps: list[dict],
    version: str,
) -> str:
    """
    Build Astro-compatible markdown.
    """

    # TODO: Can we remove this exclusion?
    today = date.today().isoformat()  # noqa: DTZ011

    md = f"""---
title: Wizard Reference
description: Reference documentation for Create Python App wizard steps.
generated: true
version: {version}
lastUpdated: {today}
tags:
  - wizard
  - reference
sidebar:
  order: 10
---

# Wizard Reference

This page is generated automatically from source code documentation.

"""

    for step_number, step in enumerate(
        steps,
        start=1,
    ):
        name = step.get(
            "Wizard Step",
            "Unknown",
        )

        title = name.replace(
            "_",
            " ",
        ).title()

        md += f"\n## Step {step_number}: {title}\n"

        if "Description" in step:
            md += f"\n### Description\n\n{step['Description']}\n"

        if "Type" in step:
            md += f"\n### Type\n\n`{step['Type']}`\n"

        if "Default" in step:
            md += f"\n### Default\n\n`{step['Default']}`\n"

        if "Options" in step:
            md += "\n### Options\n\n"

            for option in step["Options"].splitlines():
                option = option.strip()

                if option:
                    md += f"- `{option}`\n"

        if "Fields" in step:
            md += "\n### Fields\n\n"

            md += "| Field | Description |\n|-------|-------------|\n"

            fields = [
                field.strip() for field in step["Fields"].splitlines() if field.strip()
            ]

            for field in fields:
                md += f"| `{field}` | |\n"

        if "Example" in step:
            md += "\n### Example\n\n"

            examples = [
                example.strip()
                for example in step["Example"].splitlines()
                if example.strip()
            ]

            if len(examples) == 1:
                md += f"`{examples[0]}`\n"
            else:
                for example in examples:
                    md += f"- `{example}`\n"

    return md


def main() -> None:

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    source = SOURCE_FILE.read_text(encoding="utf-8")

    version = get_version()

    steps = extract_wizard_docstrings(source)

    markdown = build_markdown(
        steps,
        version,
    )

    OUTPUT_FILE.write_text(
        markdown,
        encoding="utf-8",
    )

    print(f"✅ Documentation written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
