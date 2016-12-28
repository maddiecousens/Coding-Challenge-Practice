# Write a function that returns whether two lists have the same items,
# irrespective of order.


class A(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, b):
        assert isinstance(b, A), "{} is not an intance of A".format(b)
        return self.x == b.x

    def __ne__(self, b):
        assert isinstance(b, A), "{} is not an intance of A".format(b)
        return self.x != b.x

    def __repr__(self):
        return 'A object, x={}'.format(self.x)



def same_items(lst1, lst2):
    """
    Returns T/F whether lists have same items


    >>> same_items([1,(3,4),{'a':'b'},2], [1,(3,4),{'a':'b'},2])
    True

    >>> same_items([1,(3,4),{'a':'c'},2], [1,(3,4),{'a':'b'},2])
    False

    >>> same_items([1,(3,4),{'a':'b'},A(1)], [1,(3,4),{'a':'b'},A(1)])
    True

    """

    for i, item in enumerate(lst1):
        if item != lst2[i]:
            return False

    return True


if __name__ == '__main__':

    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "All tests passed!"