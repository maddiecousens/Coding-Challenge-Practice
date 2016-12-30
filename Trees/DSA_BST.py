# Author: Problem Solving with Data Structures and Algorithms
# Source: http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
# Description:
#   
#   
# Comments by maddiecousens

class TreeNode(object):
    """
    Node class for BinarySearchTree
    """
    def __init__(self,key,val,left=None,right=None, parent=None):
        """Initialize each node to have a key, payload, leftChild, rightChild, 
        parent"""
        # What I normally call 'data'
        self.key = key
        # 'Payload' is additional info. Not entirely sure what payload would be
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        # I normall don't keep track of the parent. Will be interested to see
        # how this plays into traversal
        self.parent = parent

    def __iter__(self):
        # at first glance you might think that the code is not recursive. 
        # However, remember that __iter__ overrides the for x in operation for 
        # iteration, so it really is recursive! Because it is recursive over 
        # TreeNode instances the __iter__ method is defined in the TreeNode class.


        if self:
            if self.hasLeftChild():
                for elem in self.leftChiLd:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        """Returns left child"""
        return self.leftChild

    def hasRightChild(self):
        """Returns right child"""
        return self.rightChild

    def isLeftChild(self):
        """Return T/F whether node is a left child of it's parent"""
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """Return T/F whether node is a right child of it's parent"""
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """Return T/F whether node is the root of the tree (aka whether it doesn't
            have a parent)."""
        return not self.parent

    def isLeaf(self):
        """Return T/F whether leaf node (aka whether it doesn't have any children)"""
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """Return T/F whether node has any children"""
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """Return T/F whether node has both children"""
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        """Replace the nodes data"""
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        # set parent attribute on the new lc and rc to current node
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree(object):
    """
    Binary Search Tree Class

    """

    def __init__(self):
        """Initialize root, and number of nodes"""
        self.root = None
        self.size = 0

    def length(self):
        """Return number of nodes in tree"""
        return self.size

    def __len__(self):
        """Return number of nodes in tree"""
        return self.size

    def __iter__(self):
        """return __iter__ function on the root node"""
        return self.root.__iter__()

    # Note: if duplicate value, this adds value to the right... ideally it should
    # replace the value.

    def put(self,key,val):
        """Add a node to the tree, call _put recursively"""
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        """Recursive call to add node to BST"""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
        """
        Special method that allows you to write python statements such as:
        myZipTree['Albany'] = 94706
        """
        self.put(k,v)

    # When a matching key is found, the value stored in the payload of the node is returned.

    def get(self,key):
        """Get value at key"""
        if self.root:
            res = self._get(key,self.root)
            if res:
                   return res.payload
            else:
                   return None
        else:
            return None

    def _get(self,key,currentNode):
        """Recursive call to retrieve value from key"""
        # Return none if there isn't a node (aka called leftChild but it's None)
        if not currentNode:
            return None
        # if matching key, return node
        elif currentNode.key == key:
            return currentNode
        # if key is less than curren key, recursively call on left child
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        # if key is greater than curren key, recursively call on right child
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        """
        Allows us to write pythonic statments like z = myZipTree['Albany']. 
        """
        return self.get(key)

    def __contains__(self,key):
        """
        Allows us to write pythonic statments like 'Albany' in myZipTree
        Returns T/F

        """
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        """Delete Key"""
        # if there is more than a root node
        if self.size > 1:
            # Find node using ._get
            nodeToRemove = self._get(key,self.root)
            # if node is found
            if nodeToRemove:
                # call remove function, decrease size
                self.remove(nodeToRemove)
                self.size = self.size-1
            # otherwise raise error
            else:
              raise KeyError('Error, key not in tree')
        # if only one node, but that node is what you want to delete
        elif self.size == 1 and self.root.key == key:
            #Set root to none, decrease size
            self.root = None
            self.size = self.size - 1
        # otherwise raise error
        else:
          raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        """
        Allows you to use the 'del' operator 

        """
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,currentNode):
            # The node to be deleted has no children
            if currentNode.isLeaf(): #leaf
                if currentNode == currentNode.parent.leftChild:
                    currentNode.parent.leftChild = None
                else:
                    currentNode.parent.rightChild = None
            elif currentNode.hasBothChildren(): #interior
                succ = currentNode.findSuccessor()
                succ.spliceOut()
                currentNode.key = succ.key
                currentNode.payload = succ.payload

            else: # this node has one child
                if currentNode.hasLeftChild():
                    if currentNode.isLeftChild():
                        currentNode.leftChild.parent = currentNode.parent
                        currentNode.parent.leftChild = currentNode.leftChild
                    elif currentNode.isRightChild():
                        currentNode.leftChild.parent = currentNode.parent
                        currentNode.parent.rightChild = currentNode.leftChild
                    else:
                        currentNode.replaceNodeData(currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.leftChild.rightChild)
                else:
                    if currentNode.isLeftChild():
                        currentNode.rightChild.parent = currentNode.parent
                        currentNode.parent.leftChild = currentNode.rightChild
                    elif currentNode.isRightChild():
                        currentNode.rightChild.parent = currentNode.parent
                        currentNode.parent.rightChild = currentNode.rightChild
                    else:
                        currenturrentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)




mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])









