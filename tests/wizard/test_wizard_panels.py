from unittest.mock import patch

from create_python_app.wizard.panels import (
    show_project_details,
    show_setup_summary,
    show_welcome,
)


@patch(
    "create_python_app.wizard.panels.panel"
)
def test_show_welcome(
    mock_panel,
):
    show_welcome()

    mock_panel.assert_called_once()


@patch(
    "create_python_app.wizard.panels.panel"
)
def test_show_project_details(
    mock_panel,
):
    show_project_details(
        "my-app",
        "/projects/my-app",
        "VSCode",
        ["Python"],
    )

    mock_panel.assert_called_once()


@patch(
    "create_python_app.wizard.panels.panel"
)
def test_show_project_details_no_plugins(
    mock_panel,
):
    show_project_details(
        "my-app",
        "/projects/my-app",
        "VSCode",
        [],
    )

    mock_panel.assert_called_once()


@patch(
    "create_python_app.wizard.panels.panel"
)
@patch(
    "create_python_app.wizard.panels.apply_markup"
)
def test_show_setup_summary(
    mock_markup,
    mock_panel,
):
    show_setup_summary(
        "my-app",
        "/projects/my-app",
        "VSCode",
        ["Python"],
        ".venv",
    )

    assert mock_markup.call_count == 2
    mock_panel.assert_called_once()


@patch(
    "create_python_app.wizard.panels.panel"
)
@patch(
    "create_python_app.wizard.panels.apply_markup"
)
def test_show_setup_summary_no_plugins(
    mock_markup,
    mock_panel,
):
    show_setup_summary(
        "my-app",
        "/projects/my-app",
        "VSCode",
        [],
        ".venv",
    )

    mock_panel.assert_called_once()


