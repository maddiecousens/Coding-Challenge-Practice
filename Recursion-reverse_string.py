#Write a function that takes a string as a parameter and returns a 
#new string that is the reverse of the old string.

def reverse_string(word):
    """
    Returns string reversed

    >>> reverse_string('maddie')
    'eiddam'


    """
    if len(word) <= 1:
        return word
    return word[-1] + reverse_string(word[:-1])

if __name__ == '__main__':

    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "All tests passed!"