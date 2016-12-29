# Author: Problem Solving with Data Structures and Algorithms
# Source: http://interactivepython.org/runestone/static/pythonds/Trees/ParseTree.html
# Description:
#   Creating a data structure for a mathematical expression. Using a binary tree
#   and a stack. The stack is to keep track of the parent node.
# Comments by maddiecousens


from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    #split the exression into toekns
    fplist = fpexp.split()
    #create stack
    pStack = Stack()
    #create stree
    eTree = BinaryTree('')
    #push first tree to stack
    pStack.push(eTree)
    #set currentTree to create just created
    currentTree = eTree
    # for token in list
    for i in fplist:
        if i == '(':
            #create empty left node
            currentTree.insertLeft('')
            # push currentTree to stack, now stack has parent node when we move 
            # to the left on the next line
            pStack.push(currentTree)
            # reset currentTree to the left node
            currentTree = currentTree.getLeftChild()
        # if i is a number
        elif i not in ['+', '-', '*', '/', ')']:
            #set node value to number
            currentTree.setRootVal(int(i))
            # pop the stack to get the parent
            parent = pStack.pop()
            # move one up the tree
            currentTree = parent
        # if an operand
        elif i in ['+', '-', '*', '/']:
            # set value to operand (since we already moved to parent)
            currentTree.setRootVal(i)
            # insert new empty node to the right
            currentTree.insertRight('')
             # push currentTree to stack, now stack has parent node when we move 
            # to the left on the next line
            pStack.push(currentTree)
            # set current node to the right child
            currentTree = currentTree.getRightChild()
        elif i == ')':
            # if clothing parenthsis, move up the tree one by popping the stack
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

    def evaluate(parseTree):

        # assuming you pass in the top btree instance

        opers = {'+': operator.add, 
                 '-': operator.sub, 
                 '*': operator.mul, 
                 '/': operator.truediv}

        # get the left and right nodes
        leftC = parseTree.getLeftChild()
        rightC = parseTree.getRightChild()

        # if both nodes exist, that means the value of the current node 
        # must be an operator
        if leftC and rightC:
            # function is now equal to operator.add or operator.sub etc
            fn = opers[parseTree.getRootVal()]
            # return the function of recursive call to the left and right
            return fn(evaluate(leftC),evaluate(rightC))
        # if there are no right and left, that means its a number so just return
        # the number
        else:
            return parseTree.getRootVal()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()  #defined and explained in the next section