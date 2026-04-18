from linked_list_node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        new_node = Node(val, None)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            
        return prev
    
    def find_middle(self):
        slow = self.head
        fast= self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

def display_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    middle_node = ll.find_middle()
    print(f"Middle node value: {middle_node.val}\n")
    print("Original linked list:\n")
    display_list(ll.head)
    print("Reversing the linked list...\n")
    
    reversed_head = ll.reverse()
    
    display_list(reversed_head)