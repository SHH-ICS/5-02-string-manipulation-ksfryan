# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON


n=input("input a word")
x = 0
y = len (n)

while x <= y: 
    print (n[0:x], " ")
    x = x + 1