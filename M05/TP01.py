# Palindromes
def is_palindrome(word):
    is_sentence = 1 < len(word.split())

    if is_sentence:
        return "Sentences are not handled in this version."
    else :
        word_to_reversed_list = reversed(list(word.lower()))
        reversed_word = ''.join(word_to_reversed_list)

        return word.lower() == reversed_word

print(is_palindrome("Laval")) # True
print(is_palindrome("Radar")) # True
print(is_palindrome("Pikachu")) # False
print(is_palindrome("Erdre")) # True
print(is_palindrome("bouteille")) # False
print(is_palindrome("Hello World !")) # Sentences are not handled in this version.