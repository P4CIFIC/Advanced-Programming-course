import sys, collections

class PrimSolution():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]for row in range(vertices)]

    def get_mst_sum(self, parent):
        sum = 0
        for i in range(1, self.V):
            sum += self.graph[i][ parent[i] ]
        return sum
    
    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V 
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1 

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return self.get_mst_sum(parent)
        
  
class Graph():
    
    def __init__(self, vertices_no) -> None:
        self.vertices_no = vertices_no
        self.graph = collections.OrderedDict()
    
    def add_vertex(self, v):

        if v not in self.graph:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    def add_edge(self, v1, v2, e):

        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            temp = [v2, e]
            self.graph[v1].append(temp)
        
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
        
        """print(self.matrix)
        print(self.list_of_nodes)  """          
    
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
    
    def create_adjacency_list(self):
        self.weighted_graph = Graph(0)
        
        for element in self.list_of_nodes:
            self.weighted_graph.add_vertex(element)
        
        for i in self.list_of_nodes:
            for j in self.list_of_nodes:
                if i != j:
                    # -1 at cost to compensate for bfs misscalculation
                    self.weighted_graph.add_edge(i,j, len(self.bfs(i,j)) - 1)
        
        #self.weighted_graph.print_graph()
    
    def create_adjacency_matrix(self):
        self.prims_algo = PrimSolution(len(self.list_of_nodes))
        matrix = self.prims_algo.graph
        weighted_graph = list(self.weighted_graph.graph.items())
        
        for node in weighted_graph:
            for weight in node[1]:
                matrix[self.list_of_nodes.index(weight[0])][self.list_of_nodes.index(node[0])] = weight[1]
        
        self.prims_algo.graph = matrix
        sum = self.prims_algo.primMST()
        return sum
  

number_of_test_cases = int(input())
sums = []

while number_of_test_cases > 0:
    sp = ShortestPath("S","A", "#", input())
    sp.create_matrix()
    sp.create_adjacency_list()
    sum = sp.create_adjacency_matrix()
    sums.append(sum)
    # decrements numbers of test cases
    number_of_test_cases -= 1

for sum in sums:
    print(sum)