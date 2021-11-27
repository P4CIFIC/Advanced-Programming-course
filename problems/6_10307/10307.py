import collections

class Graph():

    # Constructs the class with an arbitrary amount of vertices
    def __init__(self, vertices_no, component_count) -> None:
        self.vertices_no = vertices_no
        self.component_count = component_count
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
          
def get_numbers_from_line(line):
    temp = line.split(" ")
    if len(temp) == 1:
        output = int(temp[0])
    else:
        output = [int(element) for element in temp]
    return output

number_of_test_cases = get_numbers_from_line(input())


while number_of_test_cases > 0:

    intial_data = get_numbers_from_line(input())
    number_of_people = intial_data[0]
    number_of_pairs = intial_data[1]
    g = Graph(0, 0)

    """ 
    The following two while loops will structure the input data into nodes
    and apply the edges for every node.
    """
    counter_num_people = 1
    counter_num_pairs = 0
    
    while counter_num_pairs != number_of_pairs:
        line = get_numbers_from_line(input())
        g.add_vertex(line[0])
        g.add_vertex(line[1])
        
        if line[0] > line[1]:
            person_one = line[1]
            person_two = line[0]
        else:
            person_one = line[0]
            person_two = line[1]
        g.add_edge(person_one, person_two)
        counter_num_pairs += 1

    g.find_components()
    # decrements numbers of test cases
    number_of_test_cases -= 1
