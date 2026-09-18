import os
from pathlib import Path


def create_project_folders(
    project_dir: Path,
    project_name: str,
):
    """
    Create the standard project folder structure.

    Creates the default directories used by
    Create Python App and populates them
    with starter files where appropriate.

    Args:
        project_dir:
            Target project directory.

        project_name:
            Name of the project.

    Returns:
        None
    """
    for folder_name in ["src", "tests", "docs"]:
        folder_path = os.path.join(project_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, ".gitkeep"), "w") as f:
            f.write("")

        # Optional starter files for each folder
        if folder_name == "src":
            # Basic package initializer for importable module
            with open(os.path.join(folder_path, "__init__.py"), "w") as f:
                f.write("# Initialize the src package\n")
            # Add a simple app entrypoint file
            with open(os.path.join(folder_path, "app.py"), "w") as f:
                f.write(
                    "def main():\n"
                    '    print("Hello from your new Python app!")\n\n'
                    'if __name__ == "__main__":\n'
                    "    main()\n"
                )

        elif folder_name == "tests":
            # Example test file so pytest/unittest runs out of the box
            with open(os.path.join(folder_path, "test_sample.py"), "w") as f:
                f.write(
                    "def test_example():\n"
                    "    assert True, 'Sample test ran successfully.'\n"
                )

        elif folder_name == "docs":
            # Placeholder README for documentation
            with open(os.path.join(folder_path, "README.md"), "w") as f:
                f.write(f"# Documentation for {project_name}\n\n")
                f.write("Describe your project here.\n")


def create_project_files(
    project_dir: Path,
    project_name: str,
):
    """
    Create root-level project files.

    Creates files such as README.md and
    pyproject.toml if they do not already
    exist.

    Args:
        project_dir:
            Target project directory.

        project_name:
            Name of the project.

    Returns:
        None
    """
    readme_path = os.path.join(project_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {project_name}\n\n")
            f.write("A Python project generated with create-python-app.\n\n")
            f.write("## Getting Started\n")
            f.write("1. Activate the virtual environment\n")
            f.write("2. Run your app:\n")
            f.write("   ```bash\n")
            f.write("   python src/app.py\n")
            f.write("   ```\n")

    pyproject_path = os.path.join(
        project_dir,
        "pyproject.toml",
    )

    if not os.path.exists(pyproject_path):
        with open(pyproject_path, "w") as f:
            f.write("[project]\n")
            f.write(f'name = "{project_name}"\n')
            f.write('version = "0.1.0"\n')
            f.write('description = ""\n')
            f.write('requires-python = ">=3.10"\n')
            f.write("dependencies = []\n")

