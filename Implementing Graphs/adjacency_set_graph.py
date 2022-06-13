"""
Skillsoft/Percipio Python Bootcamp
Course #17 Implementing Graphs

Creating an Adjaceny Set Graph

COMPLETED: 3/6/2022

Example usage:
    => g = AdjacencySetGraph(4)
    => g.add_edge(0,1)
    => g.add_edge(0,3)
    => g.add_edge(1,3)
    => g.add_edge(3,2)
    => g.show()
    returns => 
                0 --> 1
                0 --> 3
                1 --> 0
                1 --> 3
                2 --> 3
                3 --> 0
                3 --> 1
                3 --> 2

    => for i in range(4):
...       print("Adjacent to {}: {}".format(i, g.get_adjacent_vertices(i)))
    returns =>
                Adjacent to 0: [1, 3]
                Adjacent to 1: [0, 3]
                Adjacent to 2: [3]
                Adjacent to 3: [0, 1, 2]

    => for i in range(4):
...       print("In degree for vertex {}: {}".format(i, g.get_indegree(i)))
    returns =>
                In degree for vertex 0: 2
                In degree for vertex 1: 2
                In degree for vertex 2: 1
                In degree for vertex 3: 3
"""
from graph import Graph, Vertex

class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        self.vertex_list = []
        # Creates vertices i-0
        for i in range(num_vertices):
            v = Vertex(i)
            self.vertex_list.append(v)

    def add_edge(self, v1, v2, weight=1):
        """
            Attaches vertex 2 to vertex 1, as long as both vertices exist
            then attaches vertex 1 to vertex 2 if graph is NOT directed
        """
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1<0 or v2<0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))
        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights greater than 1")

        # Using the add_edge function from the Vertex() class, NOT recursive
        self.vertex_list[v1].add_edge(v2)
        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def remove_edge(self, v1, v2):
        """
            Removes vertex 2 to vertex 1, as long as both vertices exist
            then removes vertex 1 to vertex 2 if graph is NOT directed
        """ 
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1<0 or v2<0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))

        # Using the remove_edge function from the Vertex() class, NOT recursive
        self.vertex_list[v1].remove_edge(v2)
        if self.directed == False:
            self.vertex_list[v2].remove_edge(v1)
        
    def get_adjacent_vertices(self, v):
        if v<0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex {}".format(v))

        # Using the get_adjacent_vertices function from the Vertex() class, NOT recursive
        return self.vertex_list[v].get_adjacent_vertices()
    
    def is_adjacent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1<0 or v2<0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))

        # Using the is_adjacent function from the Vertex() class, NOT recursive
        return self.vertex_list[v1].is_adjacent(v2) or self.vertex_list[v2].is_adjacent(v1)

    def get_indegree(self, v):
        if v<0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex {}".format(v))

        indegree = 0
        for i in range(self.num_vertices):
            if i == v:
                continue
            if v in self.get_adjacent_vertices(i):
                indegree+=1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def show(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print("{} --> {}".format(i, v))
