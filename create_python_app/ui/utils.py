import re

from .styles import (
    MARKUP_STYLES,
    RESET,
)

ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*m")


def strip_ansi(text: str) -> str:
    """
    Remove ANSI escape sequences.
    """

    return ANSI_PATTERN.sub(
        "",
        text,
    )


def apply_markup(text: str) -> str:
    """
    Supports:

    {green}
    {/green}

    {bold}
    {/bold}

    {/}
    """

    stack = []

    pattern = r"\{(/?[a-zA-Z]+|/)\}"

    def replace(match):
        tag = match.group(1)

        if tag == "/":
            stack.clear()
            return RESET

        if tag.startswith("/"):
            style = tag[1:]

            if style in stack:
                stack.remove(style)

            result = RESET

            for active_style in stack:
                result += MARKUP_STYLES[active_style]

            return result

        if tag in MARKUP_STYLES:
            stack.append(tag)
            return MARKUP_STYLES[tag]

        return match.group(0)

    return re.sub(pattern, replace, text)
