from unittest.mock import patch

import pytest

from create_python_app.ui.keyboard import (
    Key,
    KeyPress,
    read_key,
)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_up_arrow(
    mock_getch,
):
    mock_getch.side_effect = [
        b"\xe0",
        b"H",
    ]

    result = read_key()

    assert result == KeyPress(Key.UP)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_down_arrow(
    mock_getch,
):
    mock_getch.side_effect = [
        b"\xe0",
        b"P",
    ]

    result = read_key()

    assert result == KeyPress(Key.DOWN)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_left_arrow(
    mock_getch,
):
    mock_getch.side_effect = [
        b"\xe0",
        b"K",
    ]

    result = read_key()

    assert result == KeyPress(Key.LEFT)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_right_arrow(
    mock_getch,
):
    mock_getch.side_effect = [
        b"\xe0",
        b"M",
    ]

    result = read_key()

    assert result == KeyPress(Key.RIGHT)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_unknown_extended(
    mock_getch,
):
    mock_getch.side_effect = [
        b"\xe0",
        b"X",
    ]

    result = read_key()

    assert result == KeyPress(Key.UNKNOWN)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_ctrl_c(
    mock_getch,
):
    mock_getch.return_value = b"\x03"

    with pytest.raises(KeyboardInterrupt):
        read_key()


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_enter(
    mock_getch,
):
    mock_getch.return_value = b"\r"

    result = read_key()

    assert result == KeyPress(Key.ENTER)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_backspace(
    mock_getch,
):
    mock_getch.return_value = b"\x08"

    result = read_key()

    assert result == KeyPress(Key.BACKSPACE)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_space(
    mock_getch,
):
    mock_getch.return_value = b" "

    result = read_key()

    assert result == KeyPress(Key.SPACE)


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_character(
    mock_getch,
):
    mock_getch.return_value = b"a"

    result = read_key()

    assert result == KeyPress(
        Key.CHARACTER,
        "a",
    )


@patch("create_python_app.ui.keyboard.msvcrt.getch")
def test_read_key_decode_failure(
    mock_getch,
):
    mock_getch.return_value = b"\xff"

    result = read_key()

    assert result == KeyPress(
        Key.UNKNOWN,
    )
