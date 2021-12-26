import collections

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
    
    def __init__(self, start, goal, wall, dimensions) -> None:
        self.start = start
        self.goal = goal
        self.wall = wall
        self.dimensions = dimensions
    
    def set_dimensions(self):
        temp = self.dimensions.split(" ")
        if len(temp) == 1:
            output = int(temp[0])
        else:
            output = [int(element) for element in temp]
        
        self.width = output[0]
        self.height = output[1]    

    def create_map(self):
        self.matrix = []
        self.list_of_nodes = []
    
        self.set_dimensions()

        counter_num_lines = 0
        while counter_num_lines != self.height:
            temp = [element for element in input()]
            self.matrix.append(temp)
            counter_num_lines += 1
        
        ##code for renaming the aliens (0 to n) pre-bfs algorithm
        renaming_counter = 0
        for i in range(1, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.goal:
                    self.matrix[i][j] = str(self.goal + str(renaming_counter))
                    self.list_of_nodes.append(str(self.goal + str(renaming_counter)))
                    renaming_counter += 1
        self.list_of_nodes.insert(0, self.start)

    def get_position(self, element):
        for i in range(len(self.matrix)):
            if element in self.matrix[i]:
                return (self.matrix[i].index(element), i) 
    
    def find(self, i):
        while parent[i] != i:
            i = parent[i]
        return i

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        parent[a] = b

    def kruskalMST(self, cost):
        mincost = 0

        for i in range(V):
            parent[i] = i

        edge_count = 0
        while edge_count < V - 1:
            min = INF
            a = -1
            b = -1
            for i in range(V):
                for j in range(V):
                    if self.find(i) != self.find(j) and cost[i][j] < min:
                        min = cost[i][j]
                        a = i
                        b = j
            self.union(a, b)
            edge_count += 1
            mincost += min
            
        print(mincost)

    def bfs(self, goal):
        start_position = self.get_position(self.start)
        queue = collections.deque([[start_position]])
        paths = {}
        seen = set([start_position])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if self.matrix[y][x] == goal:
                paths[self.matrix[self.get_position(goal)[0]][self.get_position(goal)[1]]] = len(path) - 1
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.width and 0 <= y2 < self.height and self.matrix[y2][x2] != self.wall and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        for path in paths:
            print(path)
            
        
                    

    def create_adjacency_matrix(self):
        cost = [[INF for column in range(len(self.list_of_nodes))]for row in range(len(self.list_of_nodes))]
        for i in self.list_of_nodes:
            self.bfs(i)
        self.kruskalMST(cost)

number_of_test_cases = int(input())

while number_of_test_cases > 0:
    sp = ShortestPath("S","A", "#", input())
    INF = float('inf')
    sp.create_map()
    V = len(sp.list_of_nodes)
    parent = [i for i in range(V)]
    sp.create_adjacency_matrix()

    number_of_test_cases -= 1