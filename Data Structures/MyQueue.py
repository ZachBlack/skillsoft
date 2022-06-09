"""
Skillsoft/Percipio Python Bootcamp

Course #13 Implementing Data Structures

COMPLETED: 2/23/2022
"""
class MyQueue:
    """Be careful enqueue on a full Queue or dequeue on an empty Queue, i.e. no exceptions"""
    def __init__(self):
        """Creates new Queue"""
        self.items = []
    
    def is_empty(self):
        """Returns True if empty"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add a new element to the end of the Queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Removes element from begining of the Queue"""
        return self.items.pop(0)

    def size(self):
        """Returns the size of the Queue"""
        return len(self.items)
    
    def peek(self):
        """Returns the first element unless the Queue is empty"""
        if self.is_empty():
            raise Exception("Nothing to peek in empty Queue")
        return self.items[0]
