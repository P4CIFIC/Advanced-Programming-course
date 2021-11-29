import collections

class Graph():

    # Constructs the class with an arbitrary amount of vertices
    def __init__(self, vertices_no) -> None:
        self.vertices_no = vertices_no
        # driver code
        self.graph = collections.OrderedDict()
    
    # Add a vertex to the dictionary
    def add_vertex(self, v):

        if v not in self.graph:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2):

        # Check if vertex v1 is a valid vertex
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            # an edge between v1 v2 does
            # imply that an edge exists between v2 and v1
            if v2 not in self.graph[v1]:
                self.graph[v1].append(v2)
            if v1 not in self.graph[v2]:
                self.graph[v2].append(v1)
                
    # Print the graph
    def print_graph(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(vertex, " -> ", edge)
          
def get_dimensions(line):
    temp = line.split(" ")
    if len(temp) == 1:
        output = int(temp[0])
    else:
        output = [int(element) for element in temp]
    return output

number_of_test_cases = int(input())


while number_of_test_cases > 0:

    intial_data = get_dimensions(input())
    x_size = intial_data[0]
    y_size = intial_data[1]
    g = Graph(0)
    coordinate_system = []
    counter_num_lines = 0
    
    while counter_num_lines != y_size:
        temp = [element for element in input()]
        coordinate_system.append(temp)
        counter_num_lines += 1

    # decrements numbers of test cases
    number_of_test_cases -= 1
