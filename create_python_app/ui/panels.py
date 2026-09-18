# TODO:
# Handle Unicode display widths correctly.
# Emoji characters may occupy 2 terminal cells
# while len() reports 1 character and may
# affect visual alignment.

# TODO:
# Content markup ANSI sequences affect
# string length calculations.

# TODO:
# ANSI markup affects alignment.
# Need custom padding calculation.

import textwrap

from .styles import BACKGROUND_STYLES, BORDER_STYLES, COLOURS, FOREGROUND_STYLES, RESET
from .utils import apply_markup, strip_ansi


def panel(
    title: str,
    content: str,
    width: int = 70,
    title_bg: str = "magenta",
    title_fg: str = "white",
    border_style: str = "magenta",
    padding: int = 1,
):
    inner_width = width - 2
    content_width = inner_width - 2

    border_colour = BORDER_STYLES.get(
        border_style,
        COLOURS["white"]["fg"],
    )

    title_bg_colour = BACKGROUND_STYLES.get(
        title_bg,
        COLOURS["magenta"]["bg"],
    )

    title_fg_colour = FOREGROUND_STYLES.get(
        title_fg,
        COLOURS["white"]["fg"],
    )

    title_text = f" {title} "

    coloured_title = f"{title_bg_colour}{title_fg_colour}{title_text}{RESET}"

    title_bar_length = inner_width - len(title_text) - 4

    empty_line = (
        f"{border_colour}│{RESET} {'':<{content_width}} {border_colour}│{RESET}"
    )

    top_border = (
        f"{border_colour}"
        "╭─ "
        + coloured_title
        + f"{border_colour}"
        + " "
        + ("─" * title_bar_length)
        + "╮"
        + RESET
    )

    print(f"{border_colour}{top_border}{RESET}")

    for _ in range(padding):
        print(empty_line)

    for line in content.splitlines():
        wrapped_lines = textwrap.wrap(line, width=content_width) or [""]

        for wrapped_line in wrapped_lines:
            styled_line = apply_markup(wrapped_line)

            visible_length = len(strip_ansi(styled_line))

            line_padding = content_width - visible_length

            print(
                f"{border_colour}│{RESET}"
                f" {styled_line}"
                f"{' ' * line_padding} "
                f"{border_colour}│{RESET}"
            )

    for _ in range(padding):
        print(empty_line)

    print(f"{border_colour}" + "╰" + "─" * inner_width + "╯" + f"{RESET}")
