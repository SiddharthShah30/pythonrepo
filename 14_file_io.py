"""
Chapter 14 — File I/O

Topics:
- Reading and writing text files
- Context managers (`with`)
- JSON serialization
"""

from pathlib import Path
import json


def write_example(path: Path, data: str):
    with path.open('w', encoding='utf-8') as f:
        f.write(data)


def read_example(path: Path) -> str:
    with path.open('r', encoding='utf-8') as f:
        return f.read()


if __name__ == "__main__":
    p = Path('example.txt')
    write_example(p, 'hello file')
    print('Read back:', read_example(p))
