class Graph:

    # Constructs the class with an arbitrary amount of vertices
    def __init__(self, vertices_no) -> None:
        self.vertices_no = vertices_no
        # driver code
        self.graph = {}

    # Add a vertex to the dictionary
    def add_vertex(self, v):
        
        if v in self.graph:
            print("Vertex ", self.v, " already exists.")
        else:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):
        
        # Check if vertex v1 is a valid vertex
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            # Since this code is not restricted to a directed or 
            # an undirected graph, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            temp = [v2, e]
            self.graph[v1].append(temp)

    # Print the graph
    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

g = Graph(0)

# stores the number of vertices in the graph
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 1)
g.add_edge(4, 1, 1)
g.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", g.graph)