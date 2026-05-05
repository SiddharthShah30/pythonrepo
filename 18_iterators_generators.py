"""
Chapter 18 — Iterators & Generators

Topics:
- Iterators protocol
- Generator functions with `yield`
- Generator expressions
"""

def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1


if __name__ == "__main__":
    print(list(count_up(5)))
