# keyboard.py

import msvcrt
from dataclasses import dataclass
from enum import Enum


class Key(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    ENTER = "enter"
    ESCAPE = "escape"
    SPACE = "space"
    BACKSPACE = "backspace"

    CHARACTER = "character"
    UNKNOWN = "unknown"


@dataclass
class KeyPress:
    key: Key
    value: str | None = None


def read_key() -> KeyPress:

    key = msvcrt.getch()

    if key in (b"\x00", b"\xe0"):
        key = msvcrt.getch()

        match key:
            case b"H":
                return KeyPress(Key.UP)

            case b"P":
                return KeyPress(Key.DOWN)

            case b"K":
                return KeyPress(Key.LEFT)

            case b"M":
                return KeyPress(Key.RIGHT)

            case _:
                return KeyPress(Key.UNKNOWN)

    if key == b"\x03":
        raise KeyboardInterrupt

    if key == b"\r":
        return KeyPress(Key.ENTER)

    if key == b"\x08":
        return KeyPress(Key.BACKSPACE)

    if key == b" ":
        return KeyPress(Key.SPACE)

    try:
        return KeyPress(Key.CHARACTER, key.decode("utf-8"))

    except UnicodeDecodeError:
        return KeyPress(Key.UNKNOWN)
