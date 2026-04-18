from linked_list_node import Node

def has_cycle_brute(head):
    seen = set()
    curr = head

    while curr:
        if id(curr) in seen:
            return True
        seen.add(id(curr))
        curr = curr.next
    return False

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if id(slow) == id(fast):
            break
    else:
        return None
    
    slow = head
    while id(slow) != id(fast):
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == "__main__":

    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(0)
    n4 = Node(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    
    
    # This will print True because there is a cycle in the linked list
    print("Brute force with cycle")
    print(has_cycle_brute(n1))
    print("Optimal with cycle")
    print(has_cycle(n1))
    
    n5 = Node(1)
    n6 = Node(2)
    n7 = Node(3)
    n5.next = n6
    n6.next = n7
    n7.next = None
    # This will print False because there is no cycle in the linked list
    print("Bruteforce solution with no cycle")
    print(has_cycle_brute(n5))
    print("Optimal solution")
    print(has_cycle(n5))