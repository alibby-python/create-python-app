from unittest.mock import patch

from create_python_app.ui.panels import panel


@patch(
    "create_python_app.ui.panels.strip_ansi"
)
@patch(
    "create_python_app.ui.panels.apply_markup"
)
def test_panel_basic(
    mock_markup,
    mock_strip,
    capsys,
):
    mock_markup.side_effect = lambda x: x
    mock_strip.side_effect = lambda x: x

    panel(
        title="Test",
        content="Hello",
    )

    output = capsys.readouterr().out

    assert "Test" in output
    assert "Hello" in output


@patch(
    "create_python_app.ui.panels.strip_ansi"
)
@patch(
    "create_python_app.ui.panels.apply_markup"
)
def test_panel_multiple_lines(
    mock_markup,
    mock_strip,
    capsys,
):
    mock_markup.side_effect = lambda x: x
    mock_strip.side_effect = lambda x: x

    panel(
        title="Test",
        content="Line 1\nLine 2",
    )

    output = capsys.readouterr().out

    assert "Line 1" in output
    assert "Line 2" in output


@patch(
    "create_python_app.ui.panels.strip_ansi"
)
@patch(
    "create_python_app.ui.panels.apply_markup"
)
def test_panel_wraps_long_text(
    mock_markup,
    mock_strip,
    capsys,
):
    mock_markup.side_effect = lambda x: x
    mock_strip.side_effect = lambda x: x

    panel(
        title="Test",
        content="A" * 200,
        width=20,
    )

    output = capsys.readouterr().out

    assert "A" in output


@patch(
    "create_python_app.ui.panels.strip_ansi"
)
@patch(
    "create_python_app.ui.panels.apply_markup"
)
def test_panel_empty_content(
    mock_markup,
    mock_strip,
    capsys,
):
    mock_markup.side_effect = lambda x: x
    mock_strip.side_effect = lambda x: x

    panel(
        title="Test",
        content="",
    )

    output = capsys.readouterr().out

    assert "Test" in output


@patch(
    "create_python_app.ui.panels.strip_ansi"
)
@patch(
    "create_python_app.ui.panels.apply_markup"
)
def test_panel_custom_colours(
    mock_markup,
    mock_strip,
):
    mock_markup.side_effect = lambda x: x
    mock_strip.side_effect = lambda x: x

    panel(
        title="Test",
        content="Hello",
        title_bg="green",
        title_fg="black",
        border_style="green",
    )


@patch(
    "create_python_app.ui.panels.strip_ansi"
)
@patch(
    "create_python_app.ui.panels.apply_markup"
)
def test_panel_invalid_colours(
    mock_markup,
    mock_strip,
):
    mock_markup.side_effect = lambda x: x
    mock_strip.side_effect = lambda x: x

    panel(
        title="Test",
        content="Hello",
        title_bg="banana",
        title_fg="potato",
        border_style="cheese",
    )
    