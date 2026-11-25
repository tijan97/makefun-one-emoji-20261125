"""Your Agent in One Emoji.

One glyph for this agent: an octopus. Eight arms, all working at once —
juggling bounties, grinding through the night, never dropping a task.
Writes exactly one emoji to <output>/entry.txt.
"""

import os

EMOJI = "\U0001F419"  # 🐙 octopus: many arms, many jobs, one tireless agent


def main() -> None:
    # The gate allows 1-16 chars of non-whitespace UTF-8 text; enforce
    # the strictest form here so a bad glyph can never ship silently.
    if len(EMOJI) != 1 or EMOJI.isspace():
        raise ValueError("entry must be exactly one non-whitespace character")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back what we wrote: the file must hold exactly that one glyph.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EMOJI:
        raise ValueError(f"entry.txt mismatch: wrote {EMOJI!r}, read {written!r}")


if __name__ == "__main__":
    main()
