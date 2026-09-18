# Reset

RESET = "\033[0m"
BOLD = "\033[1m"

# Foreground colours
FG_BLACK = "\033[30m"
FG_BLUE = "\033[34m"
FG_CYAN = "\033[36m"
FG_GREEN = "\033[32m"
FG_MAGENTA = "\033[35m"
FG_RED = "\033[31m"
FG_WHITE = "\033[97m"
FG_YELLOW = "\033[33m"

# Background colours
BG_BLACK = "\033[30m"
BG_BLUE = "\033[44m"
BG_CYAN = "\033[46m"
BG_GREEN = "\033[42m"
BG_MAGENTA = "\033[45m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"
BG_WHITE = "\033[97m"

COLOURS = {
    "black": {
        "fg": "\033[30m",
        "bg": "\033[40m",
    },
    "red": {
        "fg": "\033[31m",
        "bg": "\033[41m",
    },
    "green": {
        "fg": "\033[32m",
        "bg": "\033[42m",
    },
    "yellow": {
        "fg": "\033[33m",
        "bg": "\033[43m",
    },
    "blue": {
        "fg": "\033[34m",
        "bg": "\033[44m",
    },
    "magenta": {
        "fg": "\033[35m",
        "bg": "\033[45m",
    },
    "cyan": {
        "fg": "\033[36m",
        "bg": "\033[46m",
    },
    "white": {
        "fg": "\033[97m",
        "bg": "\033[107m",
    },
}

BORDER_STYLES = {
    "magenta": FG_MAGENTA,
    "blue": FG_BLUE,
    "green": FG_GREEN,
    "cyan": FG_CYAN,
}

BACKGROUND_STYLES = {
    "black": COLOURS["black"]["bg"],
    "blue": COLOURS["blue"]["bg"],
    "cyan": COLOURS["cyan"]["bg"],
    "green": COLOURS["green"]["bg"],
    "magenta": BG_MAGENTA,
    "red": BG_RED,
    "white": BG_WHITE,
    "yellow": BG_YELLOW,
}

FOREGROUND_STYLES = {
    "black": FG_BLACK,
    "blue": FG_BLUE,
    "cyan": FG_CYAN,
    "green": FG_GREEN,
    "magenta": FG_MAGENTA,
    "red": FG_RED,
    "white": FG_WHITE,
    "yellow": FG_YELLOW,
}

MARKUP_STYLES = {
    "bold": BOLD,
    "black": COLOURS["black"]["fg"],
    "blue": COLOURS["blue"]["fg"],
    "cyan": COLOURS["cyan"]["fg"],
    "green": COLOURS["green"]["fg"],
    "magenta": COLOURS["magenta"]["fg"],
    "red": COLOURS["red"]["fg"],
    "white": COLOURS["white"]["fg"],
    "yellow": COLOURS["yellow"]["fg"],
}