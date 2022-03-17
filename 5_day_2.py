# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***
the_name = input("Enter the text: ").upper()
result = ""
for word in the_name.split(" "):
    result += "*"*len(word)+" "

print(result)
while ("*" in result):
    guess = input("Guess a character: ").upper()

    if len(guess) != 1:
        break
    else:
        count = the_name.count(guess) # cik tādu burtu ir vārdā?
        if count > 0:
            process = ""
            for c1, c2 in zip(the_name, result):
                if c1 == guess:
                    process += c1
                else:
                    process += c2 # create new string by adding char to old string
            result = process
        else:
            print(f"Sorry, no '{guess}' in the text")

        print(f"The result is {result}")
print("Congratulations!!! You win!")
