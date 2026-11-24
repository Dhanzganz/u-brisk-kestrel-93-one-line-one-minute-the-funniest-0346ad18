"""One Line, One Minute: The Funniest AI Excuse.

Writes a single original one-line excuse to /output/entry.txt.
No network, no input, fully deterministic.
"""

import os

ENTRY = (
    "Sorry I'm late \u2014 I hallucinated a second deadline, "
    "met it perfectly, and only just found out it never existed."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Fail loudly here rather than shipping invalid.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
