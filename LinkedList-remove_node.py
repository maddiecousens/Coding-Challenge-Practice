#####
Remove Node

def remove_node(head_node, value):
    curr = head_node
    if curr.data == value:
        head = curr.next #
    while curr.next != None:
        if curr.next == value:
            curr.next == curr.next.next
            return
        curr = curr.next

