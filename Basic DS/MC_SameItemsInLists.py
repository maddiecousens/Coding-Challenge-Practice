# Write a function that returns whether two lists have the same items,
# irrespective of order.

def same_items(lst1, lst2):
    """
    Returns T/F whether lists have same items


    >>> same_items([1,3,4,2], [1,2,3,4])
    True

    >>> same_items([1,3,4,2,2], [1,2,3,4])
    False

    """

    return sorted(lst1) == sorted(lst2)


if __name__ == '__main__':

    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "All tests passed!"