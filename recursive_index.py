# HB Whiteboard Challenge

"""
Find the index of an item in a list using recursion.

Given a list of items:

>>> lst = ["hey", "there", "you"]
You should have a function that returns the 0-based index of a sought item:

>>> recursive_search("hey", lst)
0

>>> recursive_search("you")
2
If the item isn’t in the list, return None:

>>> recursive_search("porcupine", lst) is None
True
Important: Solve this problem only with recursion—you cannot use a for or while loop in your solution!
"""

def recursive_search(item, lst):

    def _recursive_search(item, lst, index):
        if not lst:
            return None
        if item == lst[0]:
            return index
        return _recursive_search(item, lst[1:], index + 1)


    print _recursive_search(item, lst, 0)