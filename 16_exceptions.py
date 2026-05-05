"""
Chapter 16 — Exceptions

Topics:
- try / except / finally
- raising exceptions
- custom exception classes
"""

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    print('safe_div(4,2)=', safe_div(4,2))
    print('safe_div(1,0)=', safe_div(1,0))
