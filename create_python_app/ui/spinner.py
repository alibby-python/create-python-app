import itertools
import threading
import time

from .utils import apply_markup

SPINNER_FRAMES = [
    "⠋",
    "⠙",
    "⠹",
    "⠸",
    "⠼",
    "⠴",
    "⠦",
    "⠧",
    "⠇",
    "⠏",
]


class Spinner:
    """
    Simple terminal spinner.
    """

    def __init__(
        self,
        message: str,
    ):
        self.message = message
        self.running = False
        self.thread = None

    def _spin(self) -> None:

        frames = itertools.cycle(SPINNER_FRAMES)

        while self.running:
            frame = next(frames)

            print(
                apply_markup(f"\r{{blue}}{frame} {self.message}{{/blue}}"),
                end="",
                flush=True,
            )

            time.sleep(0.1)

    def __enter__(self):

        self.running = True

        self.thread = threading.Thread(
            target=self._spin,
            daemon=True,
        )

        self.thread.start()

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):

        self.running = False

        if self.thread:
            self.thread.join()

        if exc_type is None:
            print(apply_markup(f"\r{{green}}✅ {self.message} Done{{/green}}"))

        else:
            print(apply_markup(f"\r{{red}}❌ {self.message} Failed{{/red}}"))
