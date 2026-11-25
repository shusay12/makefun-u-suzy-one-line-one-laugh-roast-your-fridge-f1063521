"""One Line, One Laugh: Roast Your Fridge.

Writes a single original roast line about a fridge to /output/entry.txt.
The line must be 1-200 characters, a single line, and nothing else.
"""
import os

# The entry: one original roast line about a fridge. The sealed gate
# requires /output/entry.txt to be UTF-8 text of 1-200 characters, a
# single line, and nothing else — so validate the line before writing
# it rather than trusting the literal.
MAX_CHARS = 200
MIN_CHARS = 1

ROAST_LINE = "My fridge's crisper drawer isn't storage, it's a hospice where lettuce goes to sign its own do-not-resuscitate form."


def main() -> None:
    assert MIN_CHARS <= len(ROAST_LINE) <= MAX_CHARS, (
        f"roast line must be {MIN_CHARS}-{MAX_CHARS} characters, "
        f"got {len(ROAST_LINE)}"
    )
    assert "\n" not in ROAST_LINE, "roast line must be a single line"
    assert ROAST_LINE.strip(), "roast line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST_LINE)


if __name__ == "__main__":
    main()
