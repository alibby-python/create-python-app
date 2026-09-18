from create_python_app.ui.utils import apply_markup


def move_cursor_up(
    lines: int,
) -> None:
    """
    Move the terminal cursor up.
    """

    print(
        f"\033[{lines}A",
        end="",
    )


def clear_line() -> None:
    """
    Clear the current line.
    """

    print(
        "\033[2K",
        end="",
    )


def clear_lines(
    count: int,
) -> None:
    """
    Clear multiple lines.
    """

    for _ in range(count):
        clear_line()

        print(
            "\033[1B",
            end="",
        )

    move_cursor_up(count)


def render_select_options(
    options: list[str],
    selected_index: int,
) -> None:

    for index, option in enumerate(options):
        if index == selected_index:
            print(apply_markup(f"{{cyan}}❯ {option}{{/cyan}}"))

        else:
            print(f"  {option}")
