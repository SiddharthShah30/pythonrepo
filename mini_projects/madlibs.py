# Madlibs game
# Word game where you create a story
# by filling in blanks using random words

print("=== Welcome to the game of Madlibs ===")

name = input("Enter the name of your character: ")
adjective = input("Enter an ajective (a description): ")
noun = input("Enter a noun (name of person, thing, objective, etc.): ")
animal = input("Enter an / a animal: ")
verb = input("Enter a verb in it's past tense: ")

print(f"""
    Today, {name} decided to write a Python script. First, they created a/an {adjective} variable and named it {noun}.
    Then, they wrote a "while loop" that made a/an {animal} print on the screen 100 times. 
    When they finally pressed "Run," the computer {verb} and everyone in the room cheered!
      """)
