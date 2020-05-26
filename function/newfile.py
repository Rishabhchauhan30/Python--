'''def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
    
print(is_palindrome("nitin"))'''

def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('nitin'))
