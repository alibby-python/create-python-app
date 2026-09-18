from .keyboard import (
    Key,
    read_key,
)


def input_with_default(
    prompt_text: str,
    default: str = "",
) -> str:

    buffer = list(default)

    print(
        prompt_text + default,
        end="",
        flush=True,
    )

    while True:
        keypress = read_key()

        if keypress.key == Key.ENTER:
            print()
            return "".join(buffer)

        elif keypress.key == Key.BACKSPACE:
            if buffer:
                buffer.pop()

                print(
                    "\b \b",
                    end="",
                    flush=True,
                )

        elif keypress.key == Key.CHARACTER:
            buffer.append(keypress.value)

            print(
                keypress.value,
                end="",
                flush=True,
            )
