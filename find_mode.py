#HB Whiteboard Challenge
"""
The “mode” of a list is the set of item(s) that occur the most often. For example, in [1, 2, 2, 3], 2 is the most commonly-occurring item.

Where there is a tie, the mode is all items that are tied for most common: in [1, 1, 2, 2, 3], the mode is both 1 and 2.

In this challenge, you should write a function that returns the mode.

It should always return a set, even if there’s only one item in the set:

>>> mode([1]) == {1}
True

>>> mode([1, 2, 2, 2]) == {2}
True
If there is a tie, return all:

>>> mode([1, 1, 2, 2]) == {1, 2}
True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    # START SOLUTION

    # Make dictionary of {num:frequency}

    num_count = {}

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    # Find the *count* of highest letter

    highest_count = max(num_count.values())

    # For every number with that count, add to set of mode

    mode = set()

    for num, count in num_count:
        if count == highest_count:
            mode.add(num)

    return mode