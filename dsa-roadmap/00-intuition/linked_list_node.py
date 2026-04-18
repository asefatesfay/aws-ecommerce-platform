class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def delete_node(self, node): # Not tail
        node.val = node.next.val
        node.next = node.next.next