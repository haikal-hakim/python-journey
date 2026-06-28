# --- SINGLE QUOTES AND DOUBLE QUOTES ---
print('Test')  # single quotes
print("Test")  # double quotes
print('1993')  # this is string not a number because it is enclosed in quotes
print(type('1993'))  # <class 'str'>
# The results are the same, consistent use of any quotes

# --- ESCAPE CHARACTERS ---
print('doesn\'t')  # use \' to escape the single quote
print("doesn't")  # or use double quotes instead

print("\"Yes,\" he said.")  # use \" to escape the double quote
print('"Isn\'t," she said.')  # use \' to escape the single quote

# --- SPECIAL CHARACTERS ---
s = "Hello\nWorld" # \n is a newline
print(s) # produce two lines of output using print()

# --- RAW STRINGS ---
print("C:\tnew\nfolder") # \t is a tab
print(r"C:\new\folder")
# r is a raw, meaning Python reads the string as is

# --- MULTI-LINE STRINGS ---
# string usage can span multiple lines, using triple quotes for multiline
# as well as adding \ after quotes
print("""\
      Usage: script [OPTIONS]
      -h                        Display this usage message
      -R                        Show the README and exit
      """)

# --- CONCAETENATION & REPETITION ---
print(7 * "bla" + "hh")  # blablablablablahh
# '+' concatenates, '*' repeats

# --- CONCATENATION & CONTINUATION ---
print("Herukopter")
print("Heru" "kopter")

x = ("Write the words in brackets, "
     "so Python knows that this text is continued.")
print(x)
# the use of literal concatenation is to break up long strings to make them more readable

# use '+' to concatenate variables
x = "Heru"
print(x + "kopter")  # Herukopter

# --- INDEXING ---
word = "Python"
# first character having index 0
print(word[0])  # P
print(word[5])  # n
# negative index counts from the end (right to left)
print(word[-1])  # n
print(word[-2])  # o

# --- SLICING ---
word = "Alice"
# word[start:stop] when to start and when to stop
print(word[0:2])  # Al from position 0 (included) to 2 (excluded)
print(word[1:9])  # lice Python handle out of range slice

print(word[:2])  # Al from the beginning to position 2
print(word[1:5])  # lic from position 1 to 5
print(word[-3:5])  # ce from the second-last to the end

print("B" + word[1:])  # Blice change the first character of the string
print(word[:2] + "Z")  # AlZ change the last character of the string
# +---+---+---+---+---+
# | A | l | i | c | e |
# +---+---+---+---+---+
#   0   1   2   3   4
#  -5  -4  -3  -2  -1

# --- LEN() ---
# The built-in function len() returns the length of a string
x = "abcdefghijklmnopqrstuvwxyzaaaaaaaaa"
print(len(x)) # 35
