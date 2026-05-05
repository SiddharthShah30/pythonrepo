"""
Chapter 11 — Loops

Topics:
- for loops and `range()`
- while loops
- break / continue
- nested loops

Fill exercises and examples below.
"""

def example_for():
    for i in range(5):
        print(i)


def example_while():
    n = 0
    while n < 3:
        print(n)
        n += 1


if __name__ == "__main__":
    print("Chapter 11: Loops — example outputs")
    example_for()
    example_while()
