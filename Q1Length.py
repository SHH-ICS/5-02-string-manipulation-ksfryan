# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
while True:
    word = input("Enter a word or type 'quit' to exit: ")

    if word.lower() == "quit":
        print("You have quit the program.")
        break
    
    print(f"The length of the word '{word}' is {len(word)}.")