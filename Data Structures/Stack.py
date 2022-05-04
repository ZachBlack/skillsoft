"""
Skillsoft/Percipio Python Bootcamp
Course #13 Implementing Data Structures
COMPLETED: 2/23/2022
"""
class Slack:
    """Be careful push on a full Stack or pop on an empty Stack, i.e. no exceptions"""
    def __init__(self):
        """Create a new Stack"""
        self.stack = []

    def push(self, data):
        """Add an element to the Stack"""
        self.stack.append(data)

    def pop(self):
        """Removes last element added to the Stack"""
        self.stack.pop(len(self.stack)-1)

    def is_empty(self):
        """Returns True if Stack is empty"""
        return len(self.stack) == 0

    def peek(self):
        """Returns top element of the Stack, i.e. last added element"""
        if self.is_empty():
            raise Exception("Nothing to peek in empty Stack")
        return self.stack[len(self.stack)-1]
