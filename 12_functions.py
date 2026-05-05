"""
Chapter 12 — Functions

Topics:
- Defining functions
- Parameters, defaults
- *args, **kwargs
- Docstrings and return values
"""

def greet(name, punctuation='!'):
    """Return a simple greeting."""
    return f"Hello, {name}{punctuation}"


if __name__ == "__main__":
    print(greet('Reader'))
