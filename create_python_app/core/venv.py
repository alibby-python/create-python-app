import subprocess
import sys
from pathlib import Path


def create_venv(project_dir: Path) -> str:
    """
    Create a Python virtual environment.

    Args:
        project_dir:
            Directory in which the virtual environment
            should be created.

    Returns:
        Path to the created .venv directory.
    """

    venv_path = project_dir / ".venv"

    subprocess.run(
        [
            sys.executable,
            "-m",
            "venv",
            str(venv_path),
        ],
        check=True,
    )

    return str(venv_path)
