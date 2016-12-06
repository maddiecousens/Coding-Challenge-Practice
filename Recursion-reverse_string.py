#Write a function that takes a string as a parameter and returns a 
#new string that is the reverse of the old string.

def reverse_string(word):
    if len(word) <= 1:
        return word
    return word[-1] + reverse_string(word[:-1])