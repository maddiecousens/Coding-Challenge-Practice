# Find the missing number in list of integers of length n that 
# starts with 1 and ends at n+1 

def missing_int_n2(input_lst):
    """
    Returns missing integer from list. 
    Test cases:

    >>> missing_int_n2([1,2,3,4,6])
    5

    >>> missing_int_n2([2,3,1,4,6])
    5

    >>> missing_int_n2([1,3,2,4])
    5

    >>> missing_int_n2([])
    1

    >> missing_int_n2([2,3])
    1
    """

    for i in range(1, len(input_lst) + 2):
        if i not in input_lst:
            return i

def missing_int_n(input_lst):
    """
    Returns missing integer from list. 
    Test cases:

    >>> missing_int_n([1,2,3,4,6])
    5

    >>> missing_int_n([2,3,1,4,6])
    5

    >>> missing_int_n([1,3,2,4])
    5

    >>> missing_int_n([])
    1

    >> missing_int_n([2,3])
    1
    """
    length = len(input_lst) + 1
    expected_sum = length * (length + 1) / 2
    return expected_sum - sum(input_lst) 

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print