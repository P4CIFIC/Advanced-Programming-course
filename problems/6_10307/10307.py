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
    

class ShortestPath():
    
    def __init__(self, start, goal, wall, initial_data) -> None:
        self.goal = goal
        self.wall = wall
        self.initial_data = initial_data
        self.start = start
    
    def set_dimensions(self):
        temp = self.initial_data.split(" ")
        if len(temp) == 1:
            output = int(temp[0])
        else:
            output = [int(element) for element in temp]
        
        self.width = output[0]
        self.height = output[1] 
    
    def get_position(self, element):
        for i in range(len(self.matrix)):
            if element in self.matrix[i]:
                return (self.matrix[i].index(element), i) 

    def create_matrix(self):
        self.matrix = []
        self.list_of_nodes = []
        
        self.set_dimensions()
        
        counter_num_lines = 0
        while counter_num_lines != self.height:
            temp = [element for element in input()]
            self.matrix.append(temp)
            counter_num_lines += 1
        
        ##code for renaming the aliens (0 to n) pre-djikstras algorithm
        renaming_counter = 0
        for i in range(1, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.goal:
                    self.matrix[i][j] = str(self.goal + str(renaming_counter))
                    self.list_of_nodes.append(str(self.goal + str(renaming_counter)))
                    renaming_counter += 1
        self.list_of_nodes.insert(0, self.start)
        
        print(self.matrix)
        print(self.list_of_nodes)            
                    
    
    def bfs(self, start, goal):
        start = self.get_position(start)
        queue = collections.deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if self.matrix[y][x] == goal:
                return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.width and 0 <= y2 < self.height and self.matrix[y2][x2] != self.wall and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
    
    def create_graph(self):
        self.weighted_graph = Graph(0)
        
        for element in self.list_of_nodes:
            self.weighted_graph.add_vertex(element)        
        
        for i in self.list_of_nodes:
            for j in self.list_of_nodes:
                if i != j:
                    self.weighted_graph.add_edge(i,j, len(self.bfs(i,j)) - 1)
        
        self.weighted_graph.print_graph() 


number_of_test_cases = int(input())

while number_of_test_cases > 0:
    sp = ShortestPath("S","A", "#", input())
    sp.create_matrix()
    sp.create_graph()
    # decrements numbers of test cases
    number_of_test_cases -= 1
