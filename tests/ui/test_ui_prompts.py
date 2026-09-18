from unittest.mock import Mock, patch

from create_python_app.ui.keyboard import Key
from create_python_app.ui.prompts import (
    prompt,
    checkbox_prompt,
    filepath_prompt,
    select_prompt,
)

@patch(
    "create_python_app.ui.prompts.input_with_default"
)
def test_prompt_with_default(
    mock_input,
):
    mock_input.return_value = "my-app"

    result = prompt(
        "Project name",
        default="my-app",
    )

    assert result == "my-app"

    mock_input.assert_called_once()


@patch(
    "builtins.input"
)
def test_prompt_without_default(
    mock_input,
):
    mock_input.return_value = "my-app"

    result = prompt(
        "Project name",
    )

    assert result == "my-app"

    mock_input.assert_called_once()


@patch(
    "create_python_app.ui.prompts.input_with_default"
)
def test_prompt_custom_colours(
    mock_input,
):
    mock_input.return_value = "my-app"

    prompt(
        "Project name",
        default="my-app",
        prompt_fg="green",
        text_fg="yellow",
    )

    mock_input.assert_called_once()


@patch(
    "create_python_app.ui.prompts.input_with_default"
)
def test_prompt_invalid_colour_falls_back(
    mock_input,
):
    mock_input.return_value = "my-app"

    prompt(
        "Project name",
        default="my-app",
        prompt_fg="banana",
        text_fg="potato",
    )

    mock_input.assert_called_once()


@patch(
    "create_python_app.ui.prompts.prompt"
)
def test_filepath_prompt_returns_valid_path(
    mock_prompt,
):
    mock_prompt.return_value = (
        "C:/Projects/Test"
    )

    validator = Mock(
        return_value=(True, None)
    )

    result = filepath_prompt(
        message="Location",
        default="C:/Projects/Test",
        validator=validator,
    )

    assert result == "C:/Projects/Test"

    validator.assert_called_once_with(
        "C:/Projects/Test"
    )


@patch(
    "create_python_app.ui.prompts.prompt"
)
def test_filepath_prompt_retries_until_valid(
    mock_prompt,
):
    mock_prompt.side_effect = [
        "bad-path",
        "good-path",
    ]

    validator = Mock(
        side_effect=[
            (
                False,
                "Invalid path",
            ),
            (
                True,
                None,
            ),
        ]
    )

    result = filepath_prompt(
        message="Location",
        default="C:/Projects/Test",
        validator=validator,
    )

    assert result == "good-path"

    assert validator.call_count == 2


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_select_prompt_returns_default_option(
    mock_read_key,
):
    mock_read_key.return_value = Mock(
        key=Key.ENTER
    )

    result = select_prompt(
        message="Editor",
        options=[
            "VSCode",
            "Cursor",
            "Vim",
        ],
    )

    assert result == "VSCode"


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_select_prompt_moves_down(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.DOWN),
        Mock(key=Key.ENTER),
    ]

    result = select_prompt(
        message="Editor",
        options=[
            "VSCode",
            "Cursor",
            "Vim",
        ],
    )

    assert result == "Cursor"


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_select_prompt_honours_default(
    mock_read_key,
):
    mock_read_key.return_value = Mock(
        key=Key.ENTER
    )

    result = select_prompt(
        message="Editor",
        options=[
            "VSCode",
            "Cursor",
            "Vim",
        ],
        default="Cursor",
    )

    assert result == "Cursor"


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_selects_item(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.SPACE),
        Mock(key=Key.ENTER),
    ]

    result = checkbox_prompt(
        message="Plugins",
        options=[
            "Pylance",
            "Jupyter",
        ],
    )

    assert result == [
        "Pylance",
    ]


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_selects_multiple_items(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.SPACE),
        Mock(key=Key.DOWN),
        Mock(key=Key.SPACE),
        Mock(key=Key.ENTER),
    ]

    result = checkbox_prompt(
        message="Plugins",
        options=[
            "Pylance",
            "Jupyter",
        ],
    )

    assert result == [
        "Pylance",
        "Jupyter",
    ]


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_honours_default(
    mock_read_key,
):
    mock_read_key.return_value = Mock(
        key=Key.ENTER
    )

    result = checkbox_prompt(
        message="Plugins",
        options=[
            "Pylance",
            "Jupyter",
        ],
        default=[
            "Jupyter",
        ],
    )

    assert result == [
        "Jupyter",
    ]


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_returns_empty_selection(
    mock_read_key,
):
    mock_read_key.return_value = Mock(
        key=Key.ENTER
    )

    result = checkbox_prompt(
        message="Plugins",
        options=[
            "Pylance",
            "Jupyter",
        ],
    )

    assert result == []


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_select_prompt_move_up(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.DOWN),
        Mock(key=Key.UP),
        Mock(key=Key.ENTER),
    ]

    result = select_prompt(
        "Editor",
        ["VSCode", "Cursor"],
    )

    assert result == "VSCode"


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_deselects_item(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.SPACE),
        Mock(key=Key.SPACE),
        Mock(key=Key.ENTER),
    ]

    result = checkbox_prompt(
        "Plugins",
        ["Pylance"],
    )

    assert result == []


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_handles_unknown_key(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key="UNKNOWN"),
        Mock(key=Key.ENTER),
    ]

    result = checkbox_prompt(
        "Plugins",
        ["Pylance"],
    )

    assert result == []


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_checkbox_prompt_moves_up(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.DOWN),
        Mock(key=Key.UP),
        Mock(key=Key.ENTER),
    ]

    result = checkbox_prompt(
        message="Plugins",
        options=[
            "Pylance",
            "Jupyter",
        ],
    )

    assert result == []


@patch(
    "create_python_app.ui.prompts.read_key"
)
def test_select_prompt_ignores_unknown_key(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key="UNKNOWN"),
        Mock(key=Key.ENTER),
    ]

    result = select_prompt(
        message="Editor",
        options=[
            "VSCode",
            "Cursor",
        ],
    )

    assert result == "VSCode"