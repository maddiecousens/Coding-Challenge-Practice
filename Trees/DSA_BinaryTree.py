# Author: Problem Solving with Data Structures and Algorithms
# Source: http://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html
# Description:
#   Creating a binary tree using nodes and references
# Comments by maddiecousens


# Interesting that they use a btree class opposed to a node class, but in 
# essence it's achieving the same thing
class BinaryTree:
    def __init__(self,rootObj):
        # similar to how I usually write self.data = 
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        # if there isn't a left node, simply instantiate a new BTree and 
        # adjust the leftChild attribute
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        # if there already is a left node, create a NEW BTree instance (t), 
        # set the new instances' left child to the CURRENT Btree's left child, and
        # resent CURRENT Btree's left child to the NEW BTree.
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print r.getRootVal() 
# a
print r.getLeftChild()
# None
r.insertLeft('b')
print r.getLeftChild()
# <__main__.BinaryTree instance at 0x7ff873e1cb90>
print r.getLeftChild().getRootVal()
# b
r.insertRight('c')
print r.getRightChild()
# <__main__.BinaryTree instance at 0x7ff873e19758>
print r.getRightChild().getRootVal()
# c
r.getRightChild().setRootVal('hello')
print r.getRightChild().getRootVal()
# hello