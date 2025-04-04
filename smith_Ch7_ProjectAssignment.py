#converting to lowercase
def to_lowercase(word):
    lower_word = ''
    for char in word:
        if 'A' <= char <= 'Z':
            lower_word += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            lower_word += char
    return lower_word

def is_palindrome(word):
    lower_word = to_lowercase(word)
    length = 0

    for char in lower_word:
        length += 1
    for i in range(length // 2):
        if lower_word[i] != lower_word[length - i - 1]:
            return False
    return True

user_input = input('Enter a word: ')

if is_palindrome(user_input):
    print(f'{user_input} is a palindrome.')
else:
    print(f'{user_input} is not a palindrome.')