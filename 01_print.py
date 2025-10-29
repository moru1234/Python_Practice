# Basic printing of values and types
print("My name is Moreshwar")                              # Simple string
print(10)                                                  # Integer
print((10, 20, 30))                                        # Tuple

# Printing multiple values, default separator is space
print("10", "20", "2025")                                  # Output: 10 20 2025

# Custom separators using 'sep'
print("28", "10", "2025", sep="-")                         # Output: 28-10-2025
print("28", "10", "2025", sep="/")                         # Output: 28/10/2025

# Using 'end' parameter to customize print line ending
print("28", "10", "2025", sep="-", end=";")                # Output: 28-10-2025; (no newline)
print("Next print starts on same line")                    # Output continues on same line

# Variables of different types
name = "Moreshwar"
age = 2025
address = "Pune"
height = 4.5

# Printing several values in one statement
print(name, age, address, height)                          # All separated by space by default

# Printing with labels and variables
print("Name:", name)                                       # Output: Name: Moreshwar
print("Age:", age)
print("Address:", address)
print("Height:", height)

# Demonstrating concatenation and type conversion
print("My name is " + name)                                # Concatenation (works if name is str)
# print("Age: " + age)                                     # Would give error (cannot concat str and int)
print("Age: " + str(age))                                  # Correct way: convert int to str

# Formatted printing using f-strings (modern and efficient)
print(f"My name is {name} and I live in {address}")
print(f"{name} is {age} years old and {height} feet tall.")

# Using older .format() style (still common in some codebases)
print("My name is {}, my address is {}".format(name, address))

# Advanced: Using sep and end together
print(name, age, address, height, sep="
", end="
--- End of record ---
")

# Advanced: Printing from lists using unpacking
data = [name, age, address, height]
print(*data, sep=", ")                                     # Output: Moreshwar, 2025, Pune, 4.5

# Advanced: Pretty-printing a dictionary
details = {"name": name, "age": age, "address": address, "height": height}
for key, value in details.items():
    print(f"{key.capitalize():8} : {value}")

# Learning/Catch: 
# 1. Never place positional arguments after a keyword argument in print(), e.g.,
# print(name, sep="
", age, address)  # ❌ This will error
# Always list non-keyword (positional) print arguments first, then keywords like sep=, end= last.

# 2. f-strings are preferred for readable, modern Python code.
# 3. Use sep and end for customizing output format without much string manipulation.
# 4. Always convert non-string to string when using + operator for string concatenation.

# Pro Tip: Printing to a file
with open("output.txt", "w") as file:
    print(f"{name} lives in {address}.", file=file)

# Pro Tip: Custom formatting for decimals
print(f"Height with two decimal places: {height:.2f}")

# Pro Tip: Printing with escape characters
print("Line1
Line2\tIndentedText")

# Pro Tip: Joining values with custom separator
values = ["2025", "10", "28"]
print("-".join(values))                                    # Output: 2025-10-28

# That's mastery in Python printing!