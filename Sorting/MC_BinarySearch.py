# Author: Maddie Cousens

def binary_search(lst,value):
    """Return T/F whether value is in lst"""
    assert sorted(lst) == lst, "list is not sorted, cannot perform binary search"
    
    #pointer half the list
    # if equal -- return True
    # if greater, look at upper half the list
    # if lesser, look at lower half of the list
    # if not lst - return False
    if not lst:
        return False
    
    pointer = len(lst) / 2
    
    if lst[pointer] == value:
        return True
    elif  value > lst[pointer]:
        return binary_search(lst[pointer+1:],value)
    else:
        return binary_search(lst[:pointer],value)
        
        
print binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13], 12)