# Create a program that will accept a word and output the word one letter at a time in reverse.
word = input("Enter a word to be reversed: ")

print("Your word reversed is:")

for letter in reversed(word):
    print(letter)