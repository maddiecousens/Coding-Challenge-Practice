#HB Whiteboard Challenge
"""
Given an integer, print each digit in reverse order, starting with the ones place.

For example, if you were given 1 you should simply print 1, if given 314 you should print 4, 1, 3, and if given 12 you should print 2, 1:

>>> print_digits(1)
1
>>> print_digits(314)
4
1
3
>>> print_digits(12)
2
1
"""

def reverse_int(num):
    """prints digits in reverse"""
    #handle if negative number
    if num < 0:
        num = -num

    for x in range(len(str(num))):
        print num % 10
        num = num / 10
