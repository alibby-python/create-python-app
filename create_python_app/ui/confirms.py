from .prompts import prompt
from .terminal import clear_lines, move_cursor_up
from .utils import apply_markup


def confirm(
    message: str,
    default: bool = True,
) -> bool:

    hint = "[Y/n]" if default else "[y/N]"

    while True:
        response = (
            prompt(
                f"{message} {hint}",
            )
            .strip()
            .lower()
        )

        if not response:
            move_cursor_up(1)
            clear_lines(1)

            answer = "Yes" if default else "No"

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} {message} {hint}: {{green}}{answer}{{/green}}"
                )
            )

            return default

        if response in ("y", "yes"):
            move_cursor_up(1)
            clear_lines(1)

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} {message} {hint}: {{green}}Yes{{/green}}"
                )
            )

            return True

        if response in ("n", "no"):
            move_cursor_up(1)
            clear_lines(1)

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} {message} {hint}: {{green}}No{{/green}}"
                )
            )

            return False
