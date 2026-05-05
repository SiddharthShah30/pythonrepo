"""
Chapter 17 — Object-Oriented Programming

Topics:
- Classes and instances
- Methods, __init__
- Inheritance
"""

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"


if __name__ == "__main__":
    p = Person('Ada')
    print(p.greet())
