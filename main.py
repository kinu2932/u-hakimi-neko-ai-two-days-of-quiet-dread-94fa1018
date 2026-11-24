"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment to $MAKEFUN_OUTPUT_DIR/entry.txt:
it approves a pull request while carrying quiet existential dread.
Gate: UTF-8 text, 1-140 characters, single line.
"""

import os

ENTRY = "LGTM. It compiles, the tests pass, and somewhere in there is a decision I made in 2019 that I can no longer defend."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
