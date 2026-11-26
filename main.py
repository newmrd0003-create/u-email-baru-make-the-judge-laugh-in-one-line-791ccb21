"""Make the Judge Laugh in One Line — entry writer.

This program writes entry.txt ONLY to the directory given by the
MAKEFUN_OUTPUT_DIR environment variable (fallback: /output).
It NEVER writes to the current working directory — writing to the
CWD is a REJECTED grade run_completes.
"""

import os

ENTRY = "My gym membership and I are in a toxic relationship — I pay $30 a month, it texts me 'we miss you,' and neither of us has seen the other since January."


def validate():
    """Return (True, []) if ENTRY is a valid one-liner, else (False, [reasons])."""
    reasons = []
    if not (1 <= len(ENTRY) <= 200):
        reasons.append(f"length {len(ENTRY)} not in 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        reasons.append("not a single line")
    if not ENTRY.strip():
        reasons.append("only whitespace")
    return (not reasons, reasons)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
