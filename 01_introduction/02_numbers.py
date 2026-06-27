# --- BASIC OPERATIONS ---
print(2 + 2)  # 4 addition
print(50 - 5 * 6)  # 20  subtraction & multiplication
print(8 / 5)  # 1.6 division always returns float

# --- FLOOR DIVISION & MODULUS ---
print(17 / 3)  # 5.666  classic division
print(17 // 3)  # 5 floor division (discards fractional part)
print(17 % 3)  # 2 remainder
print(5 * 3 + 2)  # 17 floored quotient * divisor + remainder

# --- EXPONENTIATION ---
print(5**2)  # 25   5 squared
print(2**7)  # 128  2 to the power of 7

# --- VARIABLES ---
width = 20
height = 5 * 9
print(width * height)  # 900

# --- MIXED TYPES ---
# integer + float = float
print(4 * 3.75 - 1)  # 14.0

# --- TYPE CONVERSION ---
print(int(3.9))  # 3 float to int
print(float(10))  # 10.0  int to float
print(str(42))  # '42' int to string
# int(), float(), str() are built-in functions to convert data types

# --- COMPLEX NUMBERS ---
c = 3 + 5j
print(c)  # (3+5j)
print(type(c))  # <class 'complex'>
# type() is a built-in Python function to check the data type of a variable.
