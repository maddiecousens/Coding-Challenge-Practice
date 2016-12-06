# Write a function that inputs a string and returns a boolean
# whether the string is an anagram of a palindrome
# - string can be a phrase


def anagram_of_palindrome(input_str):
    """Returns True if input_str is an anagram of a palindrome"""
    # Initialize default dict
    letter_dict = {}
    # Initialize odd_count
    odd_count = 0
    # Create dict of counts
    for char in input_str:
        # set default is faster than get
        letter_dict[char] = letter_dict.get(char, 0) + 1

    for char in letter_dict:
        if letter_dict[char] % 2 != 0:
            odd_count += 1
    return odd_count <= 1