#HB Whiteboard Challenge
"""
Print items from a list using recursion.

For example, if you have a list of [1, 2, 3]:

>>> print_recursively([1, 2, 3])
1
2
3
"""

def print_recursively(lst):
    if not lst:
        return
    print lst[0]
    print_recursively(lst[1:])

def print_recursively2(lst):
     if lst:
        print lst[0]
        print_recursively2(lst[1:])
