# 🐍 Python Learning Journey

A repository documenting my progress as I learn Python from the ground up — covering core concepts through hands-on code and mini projects.

---

## 📚 What's Inside

### 1. `1_variables.py` — Variables & Data Types
An introduction to Python's core data types:
- **Strings** — text wrapped in quotes
- **Integers** — whole numbers
- **Floats** — decimal numbers
- **Booleans** — `True` / `False` values

### 2. `2_typecasting.py` — Type Casting
Converting variables from one type to another using built-in functions like `str()`, `int()`, `float()`, and `bool()`. Also covers using `type()` to inspect variable types.

### 3. `3_math_functions_operators.py` — Math & Operators
A reference sheet for Python's arithmetic operators:
- Addition, subtraction, multiplication, division
- Exponentiation (`**`)
- Modulus (`%`) — finding remainders
- Shorthand assignment operators (`+=`, `-=`, etc.)

### 4. `4_input.py` — User Input
Using the `input()` function to interact with users, along with f-strings for formatted output. Includes two exercises:
- **Area of a Rectangle** — reads length and width, calculates area
- **Shopping Cart** — reads item, price, and quantity, then calculates the total

### 5. `6_logical_operator.py` — Logical Operators
Using `or`, `and`, and `not` to evaluate multiple conditions at once. Demonstrated through a weather-based event checker — tweak `temp` and `is_raining` to see how each operator affects the output.

### 6. `7_conditional_expression.py` — Conditional Expressions (Ternary Operator)
A one-line shortcut for `if-else` logic using the format `X if condition else Y`. Takes two numbers as input and checks whether each is positive/negative and even/odd, then compares which is greater.

### 7. `8_string_methods.py` — String Methods
Exploring Python's built-in string functions using a name and phone number as inputs. Covers `len()`, `find()`, `rfind()`, `replace()`, `capitalize()`, `upper()`, `lower()`, `isdigit()`, and `isalpha()`.

### 8. `9_string_indexing.py` — String Indexing & Slicing
Accessing characters in a string using the `[start:end:step]` syntax. Demonstrated on a credit card number — covers positive/negative indexing, slicing ranges, step jumps, and reversing a string.

### 9. `10_format_specifier.py` — Format Specifiers
A reference sheet for f-string formatting flags, including decimal precision (`:.2f`), spacing, zero-padding, alignment (`:<`, `:>`, `:^`), sign display (`:+`), and comma separators (`:,`).

---

## 🎮 Mini Projects

Mini projects live in the `mini_projects/` folder. Filenames inside that folder are the project names (no numeric prefixes). Run any project with `python mini_projects/<project>.py`.

Current projects in `mini_projects/`:

- `file_io_notes_app.py` — Simple notes app using file I/O and JSON storage.
- `web_title_scraper.py` — Fetches a page and prints the HTML title.
- `text_data_visualizer.py` — Console histogram of word frequencies.
- `cli_todo.py` — Small CLI todo manager using JSON storage.

### Next Chapters (suggested filenames)

Continue numbering chapters in the main folder using the same style as existing files (for example `11_loops.py`, `12_functions.py`, ...). Suggested next topics and short descriptions:

11. `11_loops.py` — Loops: `for`, `while`, `range()`, `break`/`continue`, nested loops, loop patterns and common pitfalls.

12. `12_functions.py` — Functions: defining functions, parameters, default args, `*args`/`**kwargs`, return values, scope, and docstrings.

13. `13_collections.py` — Collections: lists, tuples, dictionaries, sets, common operations and idiomatic patterns.

14. `14_file_io.py` — File I/O: reading/writing text and binary files, context managers, and JSON serialization.

15. `15_modules_packages.py` — Modules and packages: imports, `__main__`, organizing code, and a brief intro to `pip`.

16. `16_exceptions.py` — Error handling: `try`/`except`/`finally`, creating and raising custom exceptions.

17. `17_oop.py` — Object-oriented programming: classes, instances, methods, inheritance, and dunder methods.

18. `18_iterators_generators.py` — Iterators, generators, comprehensions, and lazy evaluation.

19. `19_testing.py` — Testing basics: writing simple unit tests and an intro to `pytest`.

20. `20_project.py` — Capstone project: combine multiple concepts into a small final project.

If you want, I can create skeleton files for these chapters (empty templates with headers) and commit them so you can start filling them.

---

## 🛠️ How to Run

Make sure you have Python 3 installed. Then run any file with:

```bash
python filename.py
```

For example:
```bash
python madlibs.py
```

---

## 🗺️ Topics Covered So Far

- [x] Variables & data types
- [x] Type casting
- [x] Math operators
- [x] User input & f-strings
- [x] Mini project: Madlibs
- [x] Logical operators (`or`, `and`, `not`)
- [x] Conditional expressions (ternary operator)
- [x] String methods
- [x] String indexing & slicing
- [x] Format specifiers
---
- [x] Mini project: Mini Calculator
- [x] Mini project: Temperature Converter
- [x] Mini project: Weight Converter
- [x] Mini project: Validate User Input

---

## 🚀 What's Next

- Loops (`for`, `while`)
- Functions
- Lists, tuples, and dictionaries

---

*This repo grows as I learn. Follow along for more!* 🌱
