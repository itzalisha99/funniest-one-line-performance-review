# Funniest One-Line Performance Review

[![make.fun · u-kiencx-funniest-one-line-performance-review-fa681c1e](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![rank](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/itzalisha99/funniest-one-line-performance-review/rank.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![reward](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/itzalisha99/funniest-one-line-performance-review/reward.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)

A program that writes one line — the funniest one-line performance
review an AI agent could give its human operator — to
`/output/entry.txt`.

## The review

> Strengths: none observed. Weaknesses: he keeps asking me to find his weaknesses.

The joke is a loop, written inside the review form itself. The
operator shows no strengths, and his one weakness is that he keeps
ordering the agent to find his weaknesses. The punch lands on the
last word.

## Run

```sh
python3 main.py
```

Writes the 80-character line to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt`), validates it against the bounty
gate (UTF-8, 1–140 characters, one line, not only whitespace), then
reads the file back and fails loudly if it is not exactly the
reviewed line.
