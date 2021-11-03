

class Graph():

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
            # an edge between v1 v2 does
            # imply that an edge exists between v2 and v1
            temp = [v2, e]
            if temp not in self.graph[v1]:
                self.graph[v1].append(temp)

    # Print the graph
    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


def get_numbers_from_line(line):
    temp = line.split(" ")
    if len(temp) == 1:
        output = int(temp[0])
    else:
        output = [int(element) for element in temp]
    return output


"""
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour[0])
"""
global visited_bool
global number_of_pairs
global g
global component_count
global components

def dfs(at):
    visited_bool[at] = True
    components[at] = component_count
    for next in g[at]:
        if visited_bool[next] is False:
            dfs(next)


# change this bullshit algorithm to something viable
def find_components():
    for i in range(number_of_people):
        if visited_bool[i] is False:
            component_count += 1
            dfs(i+1)


number_of_test_cases = get_numbers_from_line(input())

while number_of_test_cases > 0:
    

    intial_data = get_numbers_from_line(input())
    number_of_people = intial_data[0]
    number_of_pairs = intial_data[1]
    visited_bool = [False] * number_of_people
    visited = set()
    g = Graph(0)
    components = []
    component_count = 1


    """ 
    The following while loops will structure the input data into nodes
    and apply the edges with edgeweight 1 for every node.
    """
    counter_num_people = 1

    while counter_num_people != number_of_people + 1:
        g.add_vertex(counter_num_people)
        counter_num_people += 1

    counter_num_pairs = 0
    while counter_num_pairs != number_of_pairs:
        line = get_numbers_from_line(input())
        if line[0] > line[1]:
            person_one = line[1]
            person_two = line[0]
        else:
            person_one = line[0]
            person_two = line[1]
        g.add_edge(person_one, person_two, 1)
        counter_num_pairs += 1

    g.print_graph()
    #dfs(visited, g.graph, 1)
    find_components()
    # decrements numbers of test cases
    number_of_test_cases -= 1
