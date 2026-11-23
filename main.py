"""Entry program for the make.fun bounty "The joke about the demo".

Writes this repository's one-line joke about working beside an AI coding
agent to ``entry.txt`` inside the output directory (``$MAKEFUN_OUTPUT_DIR``,
default ``/output``). The joke itself is the whole entry; this program only
has to place it where the scorer reads it.
"""

import os
from pathlib import Path

JOKE = (
    "My AI agent swore the demo couldn't crash \u2014 and it didn't. "
    "Overnight, it had promoted the crash to production."
)

# The gate accepts 1 to 280 characters and nothing that is only whitespace.
MAX_CHARS = 280


def entry_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    if not JOKE.strip() or len(JOKE) > MAX_CHARS:
        raise ValueError("joke must be 1 to 280 non-blank characters")
    entry_path().write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
