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

### `madlibs.py` — Madlibs Game
A command-line Madlibs game! The user is prompted to enter a name, adjective, noun, animal, and verb — then the program weaves them into a funny Python-themed story.

**Sample story:**
> *Today, [name] decided to write a Python script. First, they created a/an [adjective] variable and named it [noun]. Then, they wrote a "while loop" that made a/an [animal] print on the screen 100 times. When they finally pressed "Run," the computer [verb] and everyone in the room cheered!*

### `mini_cal.py` — Mini Calculator
A simple command-line calculator. Enter an operator (`+`, `-`, `*`, `/`) and two numbers, and it computes the result using `if/elif/else` logic.

### `temperature_convertor.py` — Temperature Converter
Converts a temperature between Celsius and Fahrenheit. Takes the value and unit as input, applies the correct formula, and prints the converted result rounded to 2 decimal places.

### `weight_convertor.py` — Weight Converter
Converts weight between Kilograms and Pounds. Accepts input in either unit and outputs the converted value using the appropriate formula.

### `validate_user_input.py` — Username Validator
Validates a username against three rules: must be 15 characters or fewer, no spaces, and no digits. Uses string methods learned in `8_string_methods.py` to enforce each rule.

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
