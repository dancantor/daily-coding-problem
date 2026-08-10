'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3

'''

class Node:
    next = None
    value = None
    
    def print(self) -> None:
        current_node = self
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
            if current_node is not None:
                print("->", end=" ")
        print()
    
    def __init__(self, elements: list) -> None:
        current_node = self
        for i, element in enumerate(elements):
            current_node.value = element
            current_node.next = Node([]) if i != len(elements) - 1 else None
            current_node = current_node.next
            
    
def swap_nodes(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    
    next_node = head.next
    current_node = head
    
    while next_node is not None:
        value_aux = current_node.value
        current_node.value = next_node.value
        next_node.value = value_aux
        
        current_node = next_node.next
        next_node = None if current_node is None else current_node.next
        
    return head
    

x = Node([1, 2, 3, 4, 5])
x.print()
swap_nodes(x)
x.print()
    
