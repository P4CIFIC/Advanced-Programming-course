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
            # Since this code is not restricted to a directed or 
            # an undirected graph, an edge between v1 v2 does not
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

def solve_for_most_friends(number_of_test_cases):
    while number_of_test_cases > 0:
        intial_data = get_numbers_from_line(input())
        number_of_people = intial_data[0]
        number_of_pairs = intial_data[1]
        g = Graph(0)

        counter = 1
        while counter != number_of_people + 1:
            g.add_vertex(counter)
            counter += 1
        
        counter = 0
        while counter != number_of_pairs:
            line = get_numbers_from_line(input())
            if line[0] > line[1]:
                person_one = line[1]
                person_two = line[0]
            else:
                person_one = line[0]
                person_two = line[1]

            g.add_edge(person_one, person_two, 1)
            counter += 1

        g.print_graph()
        #decrements numbers of test cases
        number_of_test_cases -= 1
            
number_of_test_cases = get_numbers_from_line(input())
solve_for_most_friends(number_of_test_cases)