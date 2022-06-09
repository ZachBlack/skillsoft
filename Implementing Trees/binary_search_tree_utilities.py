"""
Skillsoft/Percipio Python Bootcamp
Course #17 Implementing Trees

Binary Search Tree Utilities

COMPLETED: 3/6/2022
"""

def lookup(head, data):
    if head == None:
        return print("Value not found!")
    
    if head.get_value() == data:
        return head
    
    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)

def print_node(node):
    """
        Example usuage:
            => print_node(lookup(head, 68))
            returns (if exists) => 68
    """
    if (node == None):
        print("Not found!")
    print(node.get_value())

def min_value(head):
    current = head
    while current.left != None:
        current = current.left
    return current.data

def max_value(head):
    current = head
    while current.right != None:
        current = current.right
    return current.data
