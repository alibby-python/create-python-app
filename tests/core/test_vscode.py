from pathlib import Path
from unittest.mock import Mock, patch

from create_python_app.core.vscode import (
    install_extension,
    install_vscode_extensions,
    is_extension_installed,
    setup_vscode_settings,
)


@patch("create_python_app.core.vscode.subprocess.run")
def test_is_extension_installed_returns_true(
    mock_run,
):
    mock_run.return_value = Mock(stdout="ms-python.python\n")

    assert is_extension_installed("ms-python.python")


@patch("create_python_app.core.vscode.subprocess.run")
def test_is_extension_installed_returns_false(
    mock_run,
):
    mock_run.return_value = Mock(stdout="")

    assert not is_extension_installed("ms-python.python")


@patch("create_python_app.core.vscode.subprocess.run")
def test_install_extension_calls_subprocess(
    mock_run,
):
    install_extension("ms-python.python")

    mock_run.assert_called_once_with(
        "code --install-extension ms-python.python",
        shell=True,
        check=True,
    )


@patch("create_python_app.core.vscode.platform.system")
def test_setup_vscode_settings_windows(
    mock_system,
    tmp_path,
):
    mock_system.return_value = "Windows"

    result = setup_vscode_settings(
        tmp_path,
        "C:/project/.venv",
    )

    assert result.endswith("Scripts\\python.exe")

    assert (tmp_path / ".vscode" / "settings.json").exists()


@patch("create_python_app.core.vscode.platform.system")
def test_setup_vscode_settings_linux(
    mock_system,
    tmp_path,
):
    mock_system.return_value = "Linux"

    result = setup_vscode_settings(
        tmp_path,
        "/project/.venv",
    )

    print(result)

    assert Path(result).parts[-2:] == (
        "bin",
        "python",
    )


@patch("create_python_app.core.vscode.is_extension_installed")
def test_install_vscode_extensions_already_installed(
    mock_installed,
):
    mock_installed.return_value = True

    install_vscode_extensions(
        ["Python"],
        {
            "Python": {
                "id": "ms-python.python",
            }
        },
    )


@patch("create_python_app.core.vscode.install_extension")
@patch("create_python_app.core.vscode.is_extension_installed")
def test_install_vscode_extensions_installs_extension(
    mock_installed,
    mock_install,
):
    mock_installed.return_value = False

    install_vscode_extensions(
        ["Python"],
        {
            "Python": {
                "id": "ms-python.python",
            }
        },
    )

    mock_install.assert_called_once_with("ms-python.python")
