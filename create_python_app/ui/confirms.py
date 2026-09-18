from .prompts import prompt


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
            return default

        if response in ("y", "yes"):
            return True

        if response in ("n", "no"):
            return False
