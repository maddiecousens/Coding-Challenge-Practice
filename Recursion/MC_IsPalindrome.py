"""
Write a function that takes a string as a parameter and returns 
True if the string is a palindrome, False otherwise. Remember 
that a string is a palindrome if it is spelled the same both 
forward and backward. For example: radar is a palindrome. for 
bonus points palindromes can also be phrases, but you need to 
remove the spaces and punctuation before checking. 
for example: madam i’m adam is a palindrome. Other fun palindromes include:

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota

"""

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    
    return is_palindrome(word[1:-1])

print is_palindrome('tacocat')


#other ways:

# def is_palindrome(word):
#     return word == word[::-1]