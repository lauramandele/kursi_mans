# Write the function is_palindrome (text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False

def is_palindrome(text):
    print(text)
    text = text.replace(" ", "")
    text = text.lower()
    print(text)
    reverse_text = text[::-1]
    print(reverse_text)

    return text == reverse_text


text_to_check = "Alus ari i ra    sula"
palindrome = is_palindrome(text_to_check)
print(f"Is '{text_to_check}' a palindrome? {palindrome}")