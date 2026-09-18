"""
Core utility functions for Create-Python-App.

This module handles environment creation, configuration management,
and integration with VSCode extensions.

It’s separated from the main script (`app.py`) to keep logic modular
and maintainable.
"""

import json
import platform
import subprocess
from pathlib import Path

from rich.progress import Progress, SpinnerColumn, TextColumn

from create_python_app.ui.utils import apply_markup


# --- FUNCTION DEFINITIONS ---
def is_extension_installed(ext_id: str) -> bool:
    """
    Check if a VSCode extension is already installed.

    Args:
        ext_id (str): The unique Marketplace identifier of the VSCode extension.

    Returns:
        bool: True if installed, False otherwise.

    Implementation details:
        - Executes `code --list-extensions` as a subprocess.
        - Parses stdout and checks for the given extension ID.
        - Uses `shell=True` for compatibility on Windows and UNIX systems.
    """
    result = subprocess.run(
        "code --list-extensions",
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )
    return ext_id in result.stdout.splitlines()


def install_extension(ext_id: str):
    """
    Install a VSCode extension via the command line.

    Args:
        ext_id (str): Marketplace ID (e.g., 'ms-python.python').

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: if the extension installation fails.

    Notes:
        - Relies on the `code` CLI command being available in PATH.
        - `check=True` ensures an exception is raised on failure.
    """
    subprocess.run(f"code --install-extension {ext_id}", shell=True, check=True)


def setup_vscode_settings(project_name: str, venv_path: str) -> str:
    """
    Generate a `.vscode/settings.json` file for project-specific VSCode configuration.

    Args:
        project_name (str): Path to the project root folder.
        venv_path (str): Path to the virtual environment directory.

    Returns:
        str: The Python interpreter path used in VSCode settings.

    Behavior:
        - Detects operating system via `platform.system()`.
        - On Windows → uses Scripts/python.exe.
        - On macOS/Linux → uses bin/python.
        - Creates `.vscode` folder if it doesn’t exist.
        - Writes default settings enabling Black, Flake8, and linting.
    """
    vscode_folder = Path(project_name) / ".vscode"
    vscode_folder.mkdir(exist_ok=True)

    # Determine Python path depending on OS
    system = platform.system()
    if system == "Windows":
        python_path = str(Path(venv_path) / "Scripts" / "python.exe")
    else:
        python_path = str(Path(venv_path) / "bin" / "python")

    # Define basic VSCode configuration options
    settings = {
        "python.defaultInterpreterPath": python_path,
        "python.formatting.provider": "black",
        "editor.formatOnSave": True,
        "python.linting.enabled": True,
        "python.linting.flake8Enabled": True,
    }

    # Write configuration file
    with open(vscode_folder / "settings.json", "w") as f:
        json.dump(settings, f, indent=4)

    return python_path


def install_vscode_extensions(
    plugins,
    plugin_data
):

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]Installing VSCode extensions...[/bold blue]"),
        transient=True,
    ) as progress:
        progress.add_task("extensions", total=None)

        installed = []
        already_installed = []

        for plugin_name in plugins:
            plugin_details = plugin_data.get(plugin_name)

            if plugin_details:

                ext_id = plugin_details["id"]

                if is_extension_installed(ext_id):
                    already_installed.append(plugin_name)
                else:
                    install_extension(ext_id)
                    installed.append(plugin_name)
                    print(apply_markup("{green} Done{/green}"))


    if installed:
        print(apply_markup("\n{green}{bold}Installed: {/bold}{/green}"))
        for plugin in installed:
                    print(f"   ✓ {plugin}")

    if already_installed:
        print(apply_markup("\n{yellow}{bold}Already installed:{/bold}{/yellow}"))

        for plugin in already_installed:
            print(f"   • {plugin}")
    