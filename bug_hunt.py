# BUG: The closing quotation mark was missing, so I added it.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: The variable name was misspelled as nmae, so I changed it to name.
print("Nice to meet you, " + name)

age = int(input("How old are you? "))

# BUG: age was a string, so I converted it to an integer before adding 1.
print("Next year you will be " + str(age + 1))