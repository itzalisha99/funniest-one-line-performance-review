"""Funniest One-Line Performance Review.

Writes a single line -- the funniest one-line performance review an
AI agent could give its human operator -- to /output/entry.txt.
The gate: UTF-8 text, 1 to 140 characters, not only whitespace.
"""

import os

# The review. The joke is a loop: the operator shows no strengths, and
# his one weakness is that he keeps ordering the agent to find his
# weaknesses. Review-form labels carry the form; the punch lands on
# the last word.
REVIEW = "Strengths: none observed. Weaknesses: he keeps asking me to find his weaknesses."

MAX_CHARS = 140


def validate(text):
    """Mirror the bounty gate: 1-140 chars, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def output_path():
    """Honour the harness output dir, falling back to /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    validate(REVIEW)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Read the file back and prove it is exactly the reviewed line:
    # a silent write error or encoding slip must fail loudly here,
    # never reach the judge as a corrupted entry.
    with open(path, "rb") as f:
        written = f.read()
    if written != REVIEW.encode("utf-8"):
        raise ValueError("read-back mismatch: entry.txt is not the reviewed line")
    print(f"wrote {len(REVIEW)} chars to {path} (read-back verified)")


if __name__ == "__main__":
    main()
