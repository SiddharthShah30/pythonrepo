"""
Chapter 19 — Testing

Topics:
- Writing simple unit tests with `unittest` or `pytest`
- Test structure and assertions
"""

def add(a, b):
    return a + b


if __name__ == "__main__":
    # Quick smoke checks
    assert add(1,2) == 3
    print('Basic test passed')
