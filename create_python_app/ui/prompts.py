# TODO:
# Make sure all answers have option to be color coded

from collections.abc import Callable

from .inputs import input_with_default
from .keyboard import (
    Key,
    read_key,
)
from .styles import (
    FOREGROUND_STYLES,
    RESET,
)
from .terminal import clear_lines, move_cursor_up, render_select_options
from .utils import apply_markup

PROMPT_COLOUR = FOREGROUND_STYLES["cyan"]

def prompt(
    message: str,
    default: str | None = None,
    prompt_fg: str = "cyan",
    text_fg: str = "white",
) -> str:

    prompt_colour = FOREGROUND_STYLES.get(
        prompt_fg,
        FOREGROUND_STYLES["cyan"],
    )

    text_colour = FOREGROUND_STYLES.get(
        text_fg,
        FOREGROUND_STYLES["white"],
    )    

    prompt_text = (
        f"{prompt_colour}❯{RESET} "
        f"{text_colour}{message}{RESET}"
    )

    if default:
        prompt_text += f" [{default}]"

    prompt_text += ": "

    if default:
        return input_with_default(
            prompt_text,
            default,
        )

    return input(prompt_text)


def filepath_prompt(
    message: str,
    default: str,
    validator: Callable[
        [str],
        tuple[bool, str | None],
    ],
) -> str:
    """
    Prompt the user for a directory path.

    Re-prompts until the supplied validator
    returns success.

    Args:
        message:
            Prompt message displayed to the user.

        default:
            Default path value.

        validator:
            Validation function that accepts a
            path string and returns a tuple of:

            (
                is_valid,
                error_message,
            )

    Returns:
        Validated path string.
    """

    while True:

        value = prompt(
            message,
            default=default,
            prompt_fg="cyan",
            text_fg="white",
        )

        is_valid, error_message = validator(
            value,
        )

        if is_valid:
            return value

        print(
            apply_markup(
                f"{{red}}❌ {error_message}{{/red}}"
            )
        )
        print()



def select_prompt(
    message: str,
    options: list[str],
    default: str | None = None,
) -> str:
    """
    Display a selectable list of options.

    Args:
        message:
            Prompt message.

        options:
            Available options.

    Returns:
        Selected option.
    """

    selected_index = 0

    if (
        default is not None
        and default in options
    ):
        selected_index = options.index(
            default
        )

    print(
        apply_markup(
            f"{{cyan}}❯{{/cyan}} {message}:"
        )
    )

    #
    # Render options
    #
    render_select_options(
        options,
        selected_index,
    )

    while True:

        keypress = read_key()

        if keypress.key == Key.UP:

            if selected_index > 0:
                selected_index -= 1

        elif keypress.key == Key.DOWN:

            if selected_index < len(options) - 1:
                selected_index += 1

        elif keypress.key == Key.ENTER:

            selected = options[
                selected_index
            ]

            move_cursor_up(
                len(options) + 1
            )

            clear_lines(
                len(options) + 1
            )

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} "
                    f"{message}: "
                    f"{{green}}{selected}{{/green}}"
                )
            )

            return selected

        else:
            continue

        #
        # Move back to first option
        #
        move_cursor_up(
            len(options)
        )

        #
        # Clear menu lines
        #
        clear_lines(
            len(options)
        )

        render_select_options(
            options,
            selected_index,
        )


def checkbox_prompt(
    message: str,
    options: list[str],
    default: list[str] | None = None,
    instruction: str | None = (
        "SPACE = Toggle / ENTER = Confirm"
    ),    
) -> list[str]:
    """
    Display a checkbox selection prompt.

    Args:
        message:
            Prompt message.

        options:
            Available options.

        default:
            Initially selected options.

    Returns:
        Selected options.
    """
    selected_index = 0

    selected_items: set[int] = set()

    if default:

        for index, option in enumerate(options):

            if option in default:
                selected_items.add(index)

    print(
        apply_markup(
            f"{{cyan}}❯{{/cyan}} {message}:"
        )
    )

    if instruction:
        print(
            apply_markup(
                f"   {{blue}}💡 {instruction}{{/blue}}"
            )
        )    

    def render() -> None:

        for index, option in enumerate(options):

            checked = (
                "☑"
                if index in selected_items
                else "☐"
            )

            prefix = "❯" if index == selected_index else " "

            line = (
                f"  {prefix} "
                f"{checked} "
                f"{option}"
            )

            if index == selected_index:
                print(
                    apply_markup(
                        f"{{cyan}}{line}{{/cyan}}"
                    )
                )
            else:
                print(line)

    render()

    while True:

        keypress = read_key()

        if keypress.key == Key.UP:

            if selected_index > 0:
                selected_index -= 1

        elif keypress.key == Key.DOWN:

            if selected_index < len(options) - 1:
                selected_index += 1

        elif keypress.key == Key.SPACE:

            if selected_index in selected_items:

                selected_items.remove(
                    selected_index
                )

            else:

                selected_items.add(
                    selected_index
                )

        elif keypress.key == Key.ENTER:

            selected = [
                options[index]
                for index in sorted(
                    selected_items
                )
            ]

            move_cursor_up(
                len(options) + 2
            )

            clear_lines(
                len(options) + 2
            )

            summary = (
                ", ".join(selected)
                if selected
                else "None"
            )

            print(
                apply_markup(
                    f"{{cyan}}❯{{/cyan}} "
                    f"{message}: "
                    f"{{white}}{summary}{{/white}}"
                )
            )

            return selected

        else:
            continue

        move_cursor_up(
            len(options)
        )

        clear_lines(
            len(options)
        )

        render()
        