# Author: Problem Solving with Data Structures and Algorithms
# Source: http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
# Description:
#   Writing PreOrder, InOrder, PostOrder functions to traverse tree + adjusting
#   these functions to be used in the DSA_ParseTree.py file
# Comments by maddiecousens

"""
                  5
                /    \
               9      11
              / \     / \
            14   18  19  21
           / \   /
          33 17  27

[0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
[0, 1, 2,  3,  4,  5,  6,  7,  8,  9, 10]

parent:     n / 2
left node:  2n
right node: 2n+1

ex:

18's parent:
n = 5
p = n / 2 = 2
btree[p] = 9

18's left node:
n = 5
l = 2n = 10
btree[l] = 27
"""

# Constructor
class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
# Insert
# Append to end of list (to reserve completeness)
# compare to parent and swap up the tree
    def percUp(self,i):
        # while there is still a parent
        while i / 2 > 0:
          if self.heapList[i] < self.heapList[i / 2]:
             self.heapList[i / 2], self.heapList[i] = self.heapList[i], self.heapList[i / 2]
          i = i / 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        #while node has a left child (complete trees fill left to right)
        while (i * 2) <= self.currentSize:
            # get min child
            mc = self.minChild(i)
            # if current 'node' is greater than the minimum, swap
            if self.heapList[i] > self.heapList[mc]:
                # swap
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self,i):
        # if there isn't a right child, just return the left child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        # otherwise return the lesser
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1] #top value
        self.heapList[1] = self.heapList[self.currentSize] #swap last to first
        self.currentSize = self.currentSize - 1 # subtract 1 from size
        self.heapList.pop() #remove end value
        self.percDown(1) # percolate down the swapped value
        return retval #return the deleted value

    def buildHeap(self,alist):
        i = len(alist) / 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

"""
buildHeap( [9, 6, 5, 2, 3] )
                 9
                / \
               6   5
              / \     
             2   3 
len = 5
i = 1
self.currentSize = 5
self.heapList = [0, 9, 6, 5, 2, 3]
self.percDown(2) -- 6
mc = 2
SWAP!

                 9
                / \
               2   5
              / \     
             6   3 
self.heapList = [0, 9, 2, 5, 6, 3]
i = 2 - 1 = 1
self.percDown(1)
i * 2 < current size 5
mc = index 2, 2
SWAP!
self.heapList = [0, 2, 9, 5, 6, 3]

                 2
                / \
               9   5
              / \     
             6   3 
i = minimum child = index 2 = 9
mc = index 5, 3
SWAP!
self.heapList = [0, 2, 3, 5, 6, 9]

                 2
                / \
               3   5
              / \     
             6   9 
i = 0 DONE


"""

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print bh.delMin()
print bh.delMin()
print bh.delMin()
print bh.delMin()
print bh.delMin()




