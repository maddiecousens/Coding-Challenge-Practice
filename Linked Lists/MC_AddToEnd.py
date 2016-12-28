class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution(object):
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def addToEnd(self,head,data): 
    #Complete this method
        new_node = Node(data)
        
        if head:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        else:
            head = new_node
            
        return head