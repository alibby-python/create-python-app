from .prompts import prompt
from .utils import apply_markup
from .terminal import move_cursor_up, clear_lines


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
                    f"{{cyan}}❯{{/cyan}} "
                    f"{message} {hint}: "
                    f"{{green}}{answer}{{/green}}"
                )
            )

            return default

        if response in ("y", "yes"):

            move_cursor_up(1)
            clear_lines(1)

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} "
                    f"{message} {hint}: "
                    f"{{green}}Yes{{/green}}"
                )
            )

            return True

        if response in ("n", "no"):

            move_cursor_up(1)
            clear_lines(1)

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} "
                    f"{message} {hint}: "
                    f"{{green}}No{{/green}}"
                )
            )

            return False