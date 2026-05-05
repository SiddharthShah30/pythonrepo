"""
Chapter 15 — Modules & Packages

Topics:
- Creating modules
- `if __name__ == '__main__'`
- Packages and `__init__.py`
"""

def module_func():
    return 'module says hi'


if __name__ == "__main__":
    print(module_func())
