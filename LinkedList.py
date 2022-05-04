"""
Skillsoft/Percipio Python Bootcamp
Course #13 Implementing Data Structures
COMPLETED: 2/23/2022
"""
class Node:
    """This is for a singly-Linked List"""
    def __init__(self, dataval=None, nextval=None):
        """Setting pointers to head and next Node"""
        self.dataval = dataval
        self.nextval = nextval

        def __repr__(self):
            """Returns the canonical string representation of dataval Node"""
            return repr(self.dataval)

class LinkedList:
    def __init__(self):
        """
        Creating a new singly-Linked List
            singly means only points to nextval and itself
            doubly means points to nextval, itself, AND previousval
        """
        self.head = None

    def __repr__(self):
        """Creates a string representation of the data in a list"""
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.nextval
        return '[' + '->'.join(nodes) + ']'

    def prepend(self, dataval):
        """Inserts a new element to the beginning of the Linked List"""
        self.head = Node(dataval=dataval, nextval=self.head)

    def append(self, dataval):
        """Inserts a new element to the end of a Linked List"""
        if not self.head:
            self.head = Node(dataval=dataval)
            return
        curr = self.head
        while self.nextval:
            curr = curr.nextval
        curr.nextval = Node(dataval=dataval)

    def add_after(self, middle_dataval, dataval):
        """Insert a new element after the Node with middle_dataval"""
        if middle_dataval is None:
            print('Data to insert after not specified')
            return
        curr = self.head
        while curr and (curr.dataval != middle_dataval):
            curr = curr.nextval
        new_node = Node(dataval=dataval)
        new_node.nextval = curr.nextval
        curr.nextval = new_node

    def find(self, data):
        """
        Search for the first element with 'dataval' matching 'data'
        Returns element or None if not found
        """
        curr = self.head
        while curr and (curr.dataval != data):
            curr = curr.nextval
        return curr

    def remove(self, data):
        """Removes the first occurance of 'data' in the Linked List"""
        curr = self.head
        prev = None
        while curr and (curr.dataval != data):
            prev = curr
            curr = curr.nextval
        if prev is None:
            self.head = curr.nextval
        elif curr:
            prev.nextval = curr.nextval
            curr.nextval = None

        def reverse(self):
            """Reverse the list in-place"""
            curr = self.head
            prev_node = None
            next_node = None
            while curr:
                nextval = curr.nextval
                curr.nextval = prev_node
                prev_node = currcurr = nextval
            self.head = prev_node

        def reverse_recursive(self):
            """Reverse the list in place using Recursion"""
            def recursion(curr, prev):
                if not curr:
                    return prev
                nextval = curr.nextval
                curr.nextval = prev
                prev = curr
                curr = nextval
                return recursion(curr, prev)
            self.head = recursion(curr=self.head, prev=None)

        def count_nodes(self):
            """
                Counts the number of nodes in the LinkedList
                This is Time Complexity O(N)

                To improve Time Complexity to O(1)
                initialize LinkedList with self.count=0 then increment/decrement when adjusting list size
            """
            if self.head == None:
                return 0
            else:
                curr = self.head
                count = 0
                while (curr != None):
                    curr = curr.nextval
                    count+=1
                return count