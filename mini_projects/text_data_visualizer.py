"""
Mini-project: Text data visualizer (console histogram)

Usage:
  Run and paste lines of text; a histogram of word frequencies is shown.
"""
from collections import Counter
import sys


def histogram(text, top=10):
    words = [w.strip(".,!?;:\"'()[]") for w in text.lower().split()]
    c = Counter(w for w in words if w)
    for word, count in c.most_common(top):
        print(f"{word:15} {'#' * count} ({count})")


def main():
    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        print("Enter/paste text, end with an empty line:")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == "":
                break
            lines.append(line)
        text = "\n".join(lines)
    histogram(text)


if __name__ == "__main__":
    main()
