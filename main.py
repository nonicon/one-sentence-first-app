"""One Sentence, First App — make.fun entry for "A Day of One-Line Pitches".

Writes the entry sentence to /output/entry.txt (created if missing).
One sentence, 209 characters, plain words: it tells a friend who has
never coded that their app idea can be a real, tappable thing by tonight.
The gate is checked for real before writing: 1-240 chars, a single line,
exactly one sentence (one terminal mark, none inside), and the written
file is read back to confirm it matches the entry byte for byte.
"""

import os

ENTRY = (
    "Just tell make.fun the app idea you've been carrying around in your "
    "head, and by tonight you'll be tapping through a real, working version "
    "of it \u2014 no code, no cost, just your idea finally alive on your screen."
)


def validate_entry(text: str) -> None:
    """Check the entry against the bounty gate: UTF-8 text, 1-240 chars,
    exactly one sentence."""
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry length {len(text)} out of range (1-240)")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal mark at the very end, none inside.
    if stripped[-1] not in ".!?":
        raise ValueError("entry must end with sentence-ending punctuation")
    if stripped[-2:] in ("..", "!!", "??", "!?", "?!"):
        raise ValueError("entry must end with a single sentence mark")
    for sep in (". ", "! ", "? "):
        if sep in stripped:
            raise ValueError("entry must be a single sentence")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip: the file the judge reads must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the entry sentence"
    print(f"Wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
