"""
Skillsoft/Percipio Python Bootcamp
Course #17 Implementing Trees

Defining a Binary Search Tree

COMPLETED: 3/6/2022

Example usage:
    => a = Node(45)
    => b = Node(2)
    => c = Node(33)
    => d = Node(54)
    => e = Node(25)
    => head = insert(Node, c)
    => head.print_tree()
    returns => 33
    insert(head, b)
    insert(head, e)
    head.print_tree()
    returns => 2
               25
               33   
"""

def insert(head, node):
    if head == None:
        return node
    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))
    return head

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def get_left_child(self):
        return self.left
    
    def set_left_child(self, left):
        self.left = left
        
    def get_right_child(self):
        return self.right
    
    def set_right_child(self, right):
        self.right = right
        
    def get_value(self):
        return self.data
    
    def set_value(self, value):
        self.data = value
        
    def print_tree(self):
        #In-Order Traversal of the tree
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
