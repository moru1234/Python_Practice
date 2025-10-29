# Variable declarations with different data types
name = "Moresh"        # str: used for text (string)
age = 28               # int: integer numbers
height = 4.5           # float: decimal numbers
ismarried = True       # bool: True or False
BNone = None           # NoneType: special type representing 'no value'

# Print each value and its type to understand type detection
print(f"Name      : {name}      - type is {type(name)}")          # str
print(f"Age       : {age}       - type is {type(age)}")           # int
print(f"Height    : {height}    - type is {type(height)}")        # float
print(f"isMarried : {ismarried} - type is {type(ismarried)}")     # bool
print(f"BNone     : {BNone}     - type is {type(BNone)}")         # NoneType

# Teaching: Explore lists, tuples, and dictionaries (Python's collections)

names_list = ["Moresh", "Suresh", "Ramesh"]                        # list
person_tuple = (name, age, height, ismarried)                      # tuple
person_dict = {
    "name": name,
    "age": age,
    "height": height,
    "ismarried": ismarried
}                                                                  # dict

print(f"names_list   : {names_list}   - type is {type(names_list)}")      # list
print(f"person_tuple : {person_tuple} - type is {type(person_tuple)}")    # tuple
print(f"person_dict  : {person_dict}  - type is {type(person_dict)}")     # dict

# Teaching: How to check and convert types
value = "123"
print(f"value before int: {value} - type is {type(value)}")              # str
value_int = int(value)
print(f"value after int : {value_int} - type is {type(value_int)}")      # int

# Teaching: Functions to analyze variable types
def print_type(var):
    print(f"Value: {var}, Type: {type(var)}")

print_type(3.14)
print_type(False)
print_type([1, 2, 3])

# Key tip for beginners:
# Use type(variable) to know the datatype.
# Use int(), float(), str(), list() for conversions.
# Understand that all variables in Python are objects.

'''Variables hold data of specific types: str, int, float, bool, and NoneType�.Collections include list, tuple, and dict for storing multiple values�.Type Checking with type(variable) reveals the object's type�.Type Conversion lets you transform values, e.g., string "123" to integer with int()�.Functions can display info about variables, teaching code reuse and organization�.'''