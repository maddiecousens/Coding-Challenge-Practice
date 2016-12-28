# Author: Maddie Cousens
# From: Written for Hacker Rank 30 Days of Code

# Problem: Return largest amount of edges to bottom of a binary search tree

class Node(object):
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class BinarySearchTree(object):
    # Insert method written by HackerRank
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                curr = self.insert(root.left, data)
                root.left = curr
            else:
                curr = self.insert(root.right, data)
                root.right = curr
        return root

    def getHeight_r(self, root):
        """Returns height using recursion"""

        if not root:
            return -1

        return 1 + max(self.getHeight_r(root.left), self.getHeight_r(root.right))

    def getHeight(self, root):
        """Get Height non-recursively, using a queue"""

        height = -1

        if not root:
            return 0
        
        q = []
        q.append(root)
        
        while q:
            if not q:
                return height
            
            height += 1
            
            nodes = len(q)
            
            for i in range(nodes):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return height

# Test Cases
data = [3, 5, 2, 1, 4, 6, 7]
myTree = BinarySearchTree()
root = None
for num in data:
    root = myTree.insert(root,num)

print 'Expected height 3, got', myTree.getHeight(root)
print 'Expected height 3, got', myTree.getHeight_r(root)


data = [20, 50, 35, 44, 9, 15, 62, 11, 13]
myTree = BinarySearchTree()
root = None
for num in data:
    root = myTree.insert(root,num)

print 'Expected height 4, got', myTree.getHeight(root)
print 'Expected height 4, got', myTree.getHeight_r(root)


data = [25, 39, 12, 19, 9, 23, 55, 31, 60, 35, 41, 70, 90]
myTree = BinarySearchTree()
root = None
for num in data:
    root = myTree.insert(root,num)

print 'Expected height 5, got', myTree.getHeight(root)
print 'Expected height 5, got', myTree.getHeight_r(root)