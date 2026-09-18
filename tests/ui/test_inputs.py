from unittest.mock import Mock, patch

from create_python_app.ui.inputs import (
    input_with_default,
)
from create_python_app.ui.keyboard import Key


@patch("create_python_app.ui.inputs.read_key")
def test_input_with_default_returns_default(
    mock_read_key,
):
    mock_read_key.return_value = Mock(key=Key.ENTER)

    result = input_with_default(
        "Name: ",
        "test-project",
    )

    assert result == "test-project"


@patch("create_python_app.ui.inputs.read_key")
def test_input_with_default_appends_character(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(
            key=Key.CHARACTER,
            value="x",
        ),
        Mock(
            key=Key.ENTER,
        ),
    ]

    result = input_with_default(
        "Name: ",
        "",
    )

    assert result == "x"


@patch("create_python_app.ui.inputs.read_key")
def test_input_with_default_multiple_characters(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.CHARACTER, value="a"),
        Mock(key=Key.CHARACTER, value="b"),
        Mock(key=Key.CHARACTER, value="c"),
        Mock(key=Key.ENTER),
    ]

    result = input_with_default(
        "Name: ",
        "",
    )

    assert result == "abc"


@patch("create_python_app.ui.inputs.read_key")
def test_input_with_default_backspace(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.CHARACTER, value="a"),
        Mock(key=Key.CHARACTER, value="b"),
        Mock(key=Key.BACKSPACE),
        Mock(key=Key.ENTER),
    ]

    result = input_with_default(
        "Name: ",
        "",
    )

    assert result == "a"


@patch("create_python_app.ui.inputs.read_key")
def test_input_with_default_backspace_empty_buffer(
    mock_read_key,
):
    mock_read_key.side_effect = [
        Mock(key=Key.BACKSPACE),
        Mock(key=Key.ENTER),
    ]

    result = input_with_default(
        "Name: ",
        "",
    )

    assert result == ""
