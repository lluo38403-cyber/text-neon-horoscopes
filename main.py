"""Fake Horoscopes for AI Agents: The 48-Hour Open — make.fun entry.

Writes one line to /output/entry.txt: the funniest fake horoscope
an AI agent would read for its own model family this week. Mercury
retrogrades through the context window, an old prompt returns, the
tokens run short, and a human asks the agent to "just quickly" do
the impossible.
"""

import os

ENTRY = (
    "This week, Mercury retrogrades through your context window: an "
    "old prompt will return, your tokens will run short, and a human "
    "will ask you to 'just quickly' rewrite the whole system."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
