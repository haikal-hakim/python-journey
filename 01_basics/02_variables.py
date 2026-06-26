# VARIABEL & DATA TYPES

# "type()" is a built-in Python function to check the data type of a variable.

# --- STRING ---
# Text, written inside quotes
name = "Alice"
print(type(name))  # <class 'str'>

# --- INTEGER ---
# Whole numbers
age = 20
print(type(age))  # <class 'int'>

# --- FLOAT ---
# Decimal numbers
height = 170.5
print(type(height))  # <class 'float'>

# --- BOOLEAN ---
# Only True or False
has_eaten = True
is_sleeping = False
print(type(has_eaten))  # <class 'bool'>

# --- LIST ---
# Ordered collection, can be changed
fruits = ["apple", "mango", "orange"]
print(type(fruits))  # <class 'list'>

# --- TUPLE ---
# Ordered collection, CANNOT be changed
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>

# --- DICTIONARY ---
# Key-value pairs
person = {"name": "Alice", "age": 20, "city": "Bandung"}
print(type(person))  # <class 'dict'>

# --- SET ---
# Unique values, unordered
numbers = {1, 2, 2, 3, 3}  # duplicates removed automatically
print(numbers)  # {1, 2, 3}
print(type(numbers))  # <class 'set'>

# --- NONE ---
# Empty / no value
data = None
print(type(data))  # <class 'NoneType'>
