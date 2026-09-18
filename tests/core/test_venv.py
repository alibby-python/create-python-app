from create_python_app.core.venv import (
    create_venv,
)


def test_create_venv_creates_directory(
    tmp_path,
):
    venv_path = create_venv(
        tmp_path,
    )

    assert (
        tmp_path / ".venv"
    ).exists()

    assert venv_path.endswith(
        ".venv"
    )