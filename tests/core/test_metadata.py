import json

from create_python_app.core.metadata import save_project_metadata


def test_save_project_metadata_creates_file(
    tmp_path,
):
    config = {
        "project_name": "test-project",
        "editor": "VSCode",
        "plugins": [],
    }

    file_path = save_project_metadata(
        config,
        tmp_path,
    )

    assert file_path.exists()


def test_save_project_config_writes_json(
    tmp_path,
):
    config = {
        "project_name": "test-project",
        "editor": "VSCode",
        "plugins": [],
    }

    file_path = save_project_metadata(
        config,
        tmp_path,
    )

    data = json.loads(
        file_path.read_text()
    )

    assert data["project_name"] == "test-project"