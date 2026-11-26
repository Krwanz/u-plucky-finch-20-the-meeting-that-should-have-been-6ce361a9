"""Entrypoint for the make.fun bounty
"The Meeting That Should Have Been an Email".

Writes one joke, a single line of plain text at most 200 characters,
to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

ENTRY = (
    "The email took eight seconds to write. "
    "The meeting about it took an hour, three agendas, "
    "and one 'let's circle back' \u2014 then we scheduled a follow-up."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
