import json
from pathlib import Path


def save_project_metadata(
    choices: dict,
    project_name: str,
) -> Path:
    """
    Save user-selected configuration metadata to a JSON file.

    Args:
        choices:
            Dictionary containing project metadata.

        project_name:
            Name or path of the target project directory.

    Returns:
        Path to the generated
        create_python_app_choices.json file.

    Notes:
        - Creates the file inside the project directory.
        - Overwrites any existing file.
        - Path objects are automatically converted to strings.
    """

    choices_file = Path(project_name) / "create_python_app_choices.json"

    with open(choices_file, "w") as f:
        safe_choices = {
            key: str(value) if isinstance(value, Path) else value
            for key, value in choices.items()
        }

        json.dump(
            safe_choices,
            f,
            indent=4,
        )

    return choices_file
