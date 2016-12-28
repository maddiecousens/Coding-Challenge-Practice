# Author: Maddie Cousens
# From: Written for Hacker Rank 30 Days of Code

def bubble_sort(a):
    
    swaps = 0
    for i in range(len(a) - 1):
        ## this is what was tripping me up, -1-i (i was just putting minus i)
        for j in range(len(a) - 1 - i):

            #print a, i, j, a[j], a[j+1]
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print 'Array is sorted in {} swaps.'.format(swaps)
    print 'First Element:', a[0]
    print 'Last Element:', a[-1]
    
    
bubble_sort([3,2,1])