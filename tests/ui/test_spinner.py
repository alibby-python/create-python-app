from unittest.mock import patch

from create_python_app.ui.spinner import Spinner


@patch("builtins.print")
def test_spinner_success(
    mock_print,
):
    with Spinner(
        "Testing spinner"
    ):
        pass

    assert mock_print.called


@patch("builtins.print")
def test_spinner_failure(
    mock_print,
):
    try:
        with Spinner(
            "Testing spinner"
        ):
            raise RuntimeError(
                "boom"
            )
    except RuntimeError:
        pass

    assert mock_print.called


def test_spinner_initial_state():
    spinner = Spinner(
        "Testing spinner"
    )

    assert spinner.message == (
        "Testing spinner"
    )

    assert spinner.running is False


def test_spinner_enter_returns_self():
    spinner = Spinner(
        "Testing spinner"
    )

    result = spinner.__enter__()

    assert result is spinner

    spinner.running = False

    if spinner.thread:
        spinner.thread.join()


