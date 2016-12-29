# Author: Problem Solving with Data Structures and Algorithms
# Source: http://interactivepython.org/runestone/static/pythonds/Trees/ListofListsRepresentation.html
# Description:
#   Creating a tree by list of list representation
# Comments by maddiecousens


def BinaryTree(r):
    # Basic structure
    #    node
    #     /\
    # None  None
    return [r, [], []]

def insertLeft(root,newBranch):
    # Inserting into left branch of root.
    # If left tree already exists, adding it as the left branch of new node
    #           a
    #           /\
    #          b  c
    #          /\
    #         d  e
    # [a,[b,[d,[],[]],[e,[],[]]],[c,[],[]]]
    #
    # lets say we want to add z!
    #
    #           a
    #           /\
    #          z  c
    #          /
    #         b 
    #         /\
    #        d  e
    # [a, [z, [b,[d,[],[]],[e,[],[]]], []], [c,[],[]]]

    # root = [a,[b,[d,[],[]],[e,[],[]]],[c,[],[]]]
    t = root.pop(1)
    # t = [b,[d,[],[]],[e,[],[]]]
    # root = [a,[c,[],[]]]
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
        # [a, [z, [b,[d,[],[]],[e,[],[]]], []], [c,[],[]]]
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
# [3, [], []]
insertLeft(r,4)
# [3, [4, [], []], []]
insertLeft(r,5)
# [3, [5, [4, [], []], []], []]
insertRight(r,6)
# [3, [5, [4, [], []], []], [6, [], []]]
insertRight(r,7)
# [3, [5, [4, [], []], []], [7, [], [6, [], []]]]
l = getLeftChild(r)
print l
# [5, [4, [], []], []]


setRootVal(l,9)
# [9, [4, [], []], []]
print(r)
# root value is changed because mutablility of lists
# [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
insertLeft(l,11)
# [9, [11, [4, [], []], []], []]
print r
# [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]


print getRightChild(getRightChild(r))
# [6, [], []]


"""
Final Tree

            3
            /\
           9  7
           /   \
          11    6
          /
         4
"""