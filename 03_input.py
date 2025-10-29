# Python always takes input as a string, so you need to convert (typecast) to the required type.
# Let's make input handling robust and clear. This enhanced version explains each step!

# Get user's name (string)
name = input("Enter your name: ")

# Get age and height in one line, separated by space, then convert types.
age_str, height_str = input("Enter your age and height (space-separated): ").split()
age = int(age_str)        # Convert age to integer
height = float(height_str) # Convert height to float

# Get married status in a user-friendly way:
married_input = input("Are you married? (yes/no): ").strip().lower()
if married_input in ['yes', 'y', 'true', '1']:
    is_married = True
elif married_input in ['no', 'n', 'false', '0', '']:
    is_married = False
else:
    print("Please enter yes or no for married status.")
    is_married = None # Could also reprompt user

# Print all info neatly
print("-" * 30)
print(f"Name    : {name}")
print(f"Age     : {age} years")
print(f"Height  : {height} units") # Specify units as needed
print(f"Married : {is_married}")

# --- Teaching Extension: Useful Python Input Patterns ---

# 1. Splitting multiple inputs:
# data = input("Enter a b c: ").split()   # Example: "1 2 3" => ['1', '2', '3']

# 2. Convert list of strings to integers easily:
# numbers = [int(x) for x in input("Enter numbers: ").split()]

# 3. Safely converting (with error handling):
try:
    val = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer!")

# 4. Using default values:
user = input("Enter your name (default: Guest): ") or "Guest"

# Always validate your input—never trust user input blindly for real applications!

'''Use .split() when taking multiple values at once from input.Typecast values (int(), float()) for calculations.Sanitize/validate user responses, especially for yes/no or boolean.'''