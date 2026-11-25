"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes the keeper Wi-Fi name to /output/entry.txt, exactly, with no trailing newline.
Keeper is 27 characters, pure ASCII — inside the sealed 1–32 character gate.
Pure stdlib; the grader runs python:3.13-slim with no site-packages.
"""

import os

# The turn: the ex kept the router, the narrator kept the name — and the name
# being read IS the kept name. The name is the trophy.
ENTRY = "ExKeptTheRouterIKeptTheName"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
