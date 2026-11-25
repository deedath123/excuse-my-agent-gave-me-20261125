#!/usr/bin/env python3
"""One line, one excuse: the limiter wrote the delay, I wrote the sorry."""
from pathlib import Path

ENTRY = "Boss, I missed the deadline because the rate limiter throttled my final save at 11:58, then billed me 214 tokens for the apology — the delay was its idea, the apology was mine."

def main():
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(ENTRY + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
