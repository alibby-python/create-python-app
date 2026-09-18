from unittest.mock import patch

from create_python_app.ui.confirms import confirm


@patch("create_python_app.ui.confirms.prompt")
def test_confirm_returns_default_true(
    mock_prompt,
):
    mock_prompt.return_value = ""

    assert (
        confirm(
            "Continue?",
            default=True,
        )
        is True
    )


@patch("create_python_app.ui.confirms.prompt")
def test_confirm_returns_default_false(
    mock_prompt,
):
    mock_prompt.return_value = ""

    assert (
        confirm(
            "Continue?",
            default=False,
        )
        is False
    )


@patch("create_python_app.ui.confirms.prompt")
def test_confirm_returns_true_for_yes(
    mock_prompt,
):
    mock_prompt.return_value = "yes"

    assert confirm("Continue?") is True


@patch("create_python_app.ui.confirms.prompt")
def test_confirm_returns_false_for_no(
    mock_prompt,
):
    mock_prompt.return_value = "no"

    assert confirm("Continue?") is False


@patch("create_python_app.ui.confirms.prompt")
def test_confirm_reprompts_after_invalid_response(
    mock_prompt,
):
    mock_prompt.side_effect = [
        "banana",
        "yes",
    ]

    assert confirm("Continue?") is True

    assert mock_prompt.call_count == 2
