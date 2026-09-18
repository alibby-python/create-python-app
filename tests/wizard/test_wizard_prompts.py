from unittest.mock import mock_open, patch

from create_python_app.wizard.prompts import (
    _ensure_folder,
    get_editor,
    get_plugins,
    get_project_directory,
    get_project_name,
)


def test_ensure_folder_creates_missing_folder(
    tmp_path,
):
    folder = tmp_path / "new_folder"

    result = _ensure_folder(str(folder))

    assert result == (True, None)
    assert folder.exists()


def test_ensure_folder_accepts_existing_folder(
    tmp_path,
):
    result = _ensure_folder(str(tmp_path))

    assert result == (True, None)


def test_ensure_folder_rejects_file(
    tmp_path,
):
    file_path = tmp_path / "test.txt"

    file_path.write_text("hello")

    result = _ensure_folder(str(file_path))

    assert result == (
        False,
        "This is not a valid folder path.",
    )


@patch("create_python_app.wizard.prompts.prompt")
def test_get_project_name(
    mock_prompt,
):
    mock_prompt.return_value = "my-app"

    result = get_project_name()

    assert result == "my-app"


@patch("create_python_app.wizard.prompts.filepath_prompt")
def test_get_project_directory(
    mock_filepath_prompt,
):
    mock_filepath_prompt.return_value = "C:/Projects/Test"

    result = get_project_directory("C:/Projects/Test")

    assert result == "C:/Projects/Test"


@patch("create_python_app.wizard.prompts.select_prompt")
def test_get_editor(
    mock_select_prompt,
):
    mock_select_prompt.return_value = "VSCode"

    result = get_editor("VSCode")

    assert result == "VSCode"


@patch("create_python_app.wizard.prompts.Path.exists")
def test_get_plugins_no_plugin_file(
    mock_exists,
):
    mock_exists.return_value = False

    plugins, data = get_plugins("VSCode")

    assert plugins == []
    assert data == {}


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="""
    {
        "PluginA": {
            "editors": ["PyCharm"],
            "id": "example"
        }
    }
    """,
)
@patch("create_python_app.wizard.prompts.Path.exists")
def test_get_plugins_no_matching_plugins(
    mock_exists,
    mock_file,
):
    mock_exists.return_value = True

    plugins, data = get_plugins("VSCode")

    assert plugins == []
    assert data == {}


@patch("create_python_app.wizard.prompts.checkbox_prompt")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="""
    {
        "Pylance": {
            "id": "ms-python.vscode-pylance",
            "editors": ["VSCode"]
        }
    }
    """,
)
@patch("create_python_app.wizard.prompts.Path.exists")
def test_get_plugins_returns_selection(
    mock_exists,
    mock_file,
    mock_checkbox,
):
    mock_exists.return_value = True

    mock_checkbox.return_value = ["Pylance"]

    plugins, plugin_data = get_plugins("VSCode")

    assert plugins == ["Pylance"]

    assert "Pylance" in plugin_data
