from create_python_app.ui.utils import (
    apply_markup,
    strip_ansi,
)


def test_strip_ansi():
    text = "\033[31mHello\033[0m"

    result = strip_ansi(text)

    assert result == "Hello"


def test_apply_markup_opening_tag():
    result = apply_markup("{green}Hello{/}")

    assert "Hello" in result


def test_apply_markup_closing_tag():
    result = apply_markup("{green}Hello{/green}")

    assert "Hello" in result


def test_apply_markup_unknown_tag():
    result = apply_markup("{banana}Hello{/banana}")

    assert "{banana}" in result
