"""
Skillsoft/Percipio Python Bootcamp
Course #17 Implementing Trees

Binary Search Tree Traversal
NOTE: The Queue data structure is used in Breadth First Traversal, import it

COMPLETED: 3/6/2022
"""
from data_structures.MyQueue import MyQueue

def breadth_first(node):
    if(node == None):
        raise Exception("No root found!")
    
    path = []
    queue = MyQueue()
    queue.enqueue(node)
    
    while queue.size() == 0:
        current = queue.dequeue()
        path.append(current.data)

        if current.get_left_child() != None:
            queue.enqueue(current.get_left_child())

        if current.get_right_child() != None:
            queue.enqueue(current.get_right_child())
    
    return path

def pre_order(node):
    path = []
    if node:
        path.append(node.data)
        path += pre_order(node.get_left_child())
        path += pre_order(node.get_right_child())
    return path

def in_order(node):
    path = []
    if node:
        path += in_order(node.get_left_child())
        path.append(node.data)
        path += in_order(node.get_right_child())
    return path

def post_order(node):
    path = []
    if node:
        path += post_order(node.get_left_child())
        path += post_order(node.get_right_child())
        path.append(node.data)
    return path
