from linked_list_node import Node

def remove_nth_brute(head, n):
    curr = head
    length = 0

    while curr:
        length += 1
        curr = curr.next
    if n > length:
        return head
    
    dummy = Node(0, head)
    curr = dummy
    for _ in range(length - n):
        curr = curr.next
    
    curr.next = curr.next.next
    return dummy.next

def remove_nth(head, n):
    dummy = Node(0, head)
    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next

def display_list(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    n = 2
    new_list = remove_nth_brute(n1, n)

    curr = new_list

    display_list(curr)

    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)

    n6.next = n7
    n7.next = n8
    n8.next = n9
    n9.next = n10
    n10.next = n11
    
    print("Optimal solution \n")
    another_list = remove_nth(n6, 3)
    curr = another_list
    display_list(curr)

