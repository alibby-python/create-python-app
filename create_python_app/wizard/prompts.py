import json
import os
from pathlib import Path

from create_python_app.ui.prompts import (
    checkbox_prompt,
    filepath_prompt,
    prompt,
    select_prompt,
)
from create_python_app.ui.utils import apply_markup


def _ensure_folder(
    path: str,
) -> tuple[bool, str | None]:
    """
    Validate a project directory path.

    Creates the directory if it does not
    already exist.

    Args:
        path:
            Directory path supplied by the user.

    Returns:
        Tuple containing a success flag and
        optional validation message.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        return True, None  # Successfully created
    if not os.path.isdir(path):
        return False, "This is not a valid folder path."
    return True, None


def get_project_name() -> str:
    """
    Prompt for a project name.

    Returns:
        User-supplied project name.
    """
    return prompt(
        "What is your project name?",
        default="my-python-app",
        prompt_fg="blue",
        text_fg="white",
    )


def get_project_directory(
    default_project_path: str,
) -> str:
    """
    Prompt for a project directory.

    Args:
        default_project_path:
            Default location suggested to
            the user.

    Returns:
        Selected project directory path.
    """
    return filepath_prompt(
        message="Where should we create this project?",
        default=default_project_path,
        validator=_ensure_folder,
    )


def get_editor(default_editor):
    return select_prompt(
        message="Choose your editor",
        options=[
            "VSCode",
            "Cursor",
            "Vim",
            "Other",
        ],
        default=default_editor,
    )


def get_plugins(
    editor: str,
) -> tuple[list[str], dict]:
    """
    Prompt for optional editor plugins.

    Args:
        editor:
            Selected editor.

    Returns:
        Tuple containing selected plugin
        names and plugin metadata.
    """
    plugins_file = Path(__file__).parent.parent / "data" / "plugins.json"

    if plugins_file.exists():
        with open(plugins_file, "r", encoding="utf-8") as f:
            plugin_data = json.load(f)
    else:
        plugin_data = {}

    available_plugins = {
        name: details
        for name, details in plugin_data.items()
        if editor in details["editors"]
    }

    if not available_plugins:
        print()
        print(
            apply_markup(
                "{blue}{bold}💡 Plugin installation is currently available for VS Code only.{/bold}{/blue}"
            )
        )

        return [], {}

    selected_plugins = checkbox_prompt(
        message="Select packages",
        options=list(available_plugins.keys()),
        instruction=("SPACE = Select/Deselect, ENTER = Continue"),
    )

    return (
        selected_plugins,
        available_plugins,
    )
