# Author: Problem Solving with Data Structures and Algorithms
# Source: http://interactivepython.org/runestone/static/pythonds/Trees/TreeTraversals.html
# Description:
#   Writing PreOrder, InOrder, PostOrder functions to traverse tree + adjusting
#   these functions to be used in the DSA_ParseTree.py file
# Comments by maddiecousens


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# If the traversal is on the class it looks like this:
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# Evaluate a Parse tree using post order recursion
# This is the same as the evaluate function in DSA_ParseTree.py, except modelled
# more similarly to postorder() above.

def postordereval(tree):
    opers = {'+':operator.add, 
             '-':operator.sub, 
             '*':operator.mul, 
             '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

# In order traversal is similar to rewriting the expression of a parse tree
#           +
#           /\
#          3  *
#             /\
#            4  5
#
# "(" + "3" + "+" + "(4" + '*' '5') + ")"
# "(3+(4*5))"
def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

