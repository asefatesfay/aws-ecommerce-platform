from linked_list_node import Node

if __name__ == "__main__":
    n1 = Node(4)
    n2 = Node(5)
    n3= Node(1)
    n4 = Node(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    node_to_delete = n2
    node_to_delete.delete_node(node_to_delete)

    current = n1
    while current:
        print(current.val)
        current = current.next




