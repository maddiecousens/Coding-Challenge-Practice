

def dicts_same(dict1, dict2):
    """
    returns whether dictionaries are the dicts_same

    >>> dicts_same({'a':{'b':1,'c':2}}, {'a':{'b':1,'c':2}})
    True

    >>> dicts_same({'a':{'b':2,'c':2}}, {'a':{'b':1,'c':2}})
    False

    >>> dicts_same({'a':{'b':1,'c':3}}, {'a':{'b':1,'c':2}})
    False

    >>> dicts_same({'a':{'b':1,'c':2}, 'b':{'d':1,'e':2}}, {'a':{'b':1,'c':2}, 'b':{'d':1,'e':2}})
    True

    >>> dicts_same({'a':{'b':1,'c':2}, 'b':{'d':1,'e':2}, 'c':5}, {'a':{'b':1,'c':2}, 'b':{'d':1,'e':2}})
    False

    >>> dicts_same({'a':{'b':1,'c':2}, 'b':{'d':2,'e':2}}, {'a':{'b':1,'c':2}, 'b':{'d':1,'e':2}})
    False

    >>> dicts_same({'a':{'b':1,'c':2}, 'b':{'d':1,'e':2}}, {'a':{'b':1,'c':3}, 'b':{'d':1,'e':2}})
    False

    """

    for key, val in dict1.iteritems():

        if key in dict2:
            if type(val) is dict and type(dict2[key]) is dict:
                dicts_same(val, dict2[key])

            if val != dict2[key]:
                return False

        else:
            return False

    return True




if __name__ == '__main__':
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print 'All tests passed!'