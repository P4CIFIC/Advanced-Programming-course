import collections
import time
import sys

class Prims():
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        sum = 0
        for i in range(1, self.V):
            sum+=self.graph[i][parent[i]]
        print(sum)

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
        start = time.time()
        print("prims")
        
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        if self.V < 1:
            return
        key[0] = 0
        
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        end = time.time()
        print(end - start)
        self.printMST(parent)
  
class ShortestPath():
    
    
    def __init__(self, start, goal, wall, dimensions) -> None:
        self.start = start
        self.goal = goal
        self.wall = wall
        self.dimensions = dimensions
        self.start_position = 0
    
    
    def set_dimensions(self):
        temp = self.dimensions.split(" ")
        if len(temp) == 1:
            output = int(temp[0])
        else:
            output = [int(element) for element in temp]
        
        self.width = output[0]
        self.height = output[1]
        
    
    
    def create_map(self):
        print("create map")
        start = time.time()
        self.matrix = []
        self.list_of_nodes = collections.OrderedDict()
    
        self.set_dimensions()

        ## takes input and converts it to 2d array
        counter_num_lines = 0
        while counter_num_lines != self.height:
            temp = [element for element in input()]
            self.matrix.append(temp)
            counter_num_lines += 1
        
        ## code for renaming the aliens (0 to n) pre-bfs algorithm and creating dict of known nodes with pos 
        renaming_counter = 0
        for i in range(1, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.goal:
                    self.matrix[i][j] = str(self.goal + str(renaming_counter))
                    self.list_of_nodes[str(self.goal + str(renaming_counter))] = (j,i)
                    renaming_counter += 1
                elif self.matrix[i][j] == self.start:
                    self.list_of_nodes["S"] = (j,i) 
        end = time.time()
        print(end - start)
        
        
    
    """def find(self, i):
        while parent[i] != i:
            i = parent[i]
        return i

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        parent[a] = b
    
    def kruskalMST(self, cost):
        start = time.time()
        print("kriskat mst")
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
        end = time.time()
        print(end - start)
        print("\n\n")"""
        

    """def bfs(self, start, goal):
        
        queue = collections.deque([[start]])
        paths = {}
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if self.matrix[y][x] == goal:
                paths[self.matrix[self.list_of_nodes.get(goal)[0]][self.list_of_nodes.get(goal)[1]]] = len(path) - 1
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.width and 0 <= y2 < self.height and self.matrix[y2][x2] != self.wall and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        print(paths)"""
    
    def bfs(self, nodes, cost):
        starttime = time.time()
        print("bfs")
        for i in range (len(nodes)):
            start = nodes[i][1]
            queue = collections.deque([[start]])
            seen = set([start])

            # this contains all the paths found
            found_paths = {}

            # search flag recording the shortest distance
            #min_path_length = None

            while queue:
                path = queue.popleft()

                # check if we already passed the min_path_length's level
                """if min_path_length is not None and min_path_length < len(path):
                    break"""

                x, y = path[-1]
                if (x,y) in self.list_of_nodes.values():
                    key_for_value = list(self.list_of_nodes.keys())[list(self.list_of_nodes.values()).index((x,y))]
                    if self.matrix[y][x] == key_for_value:
                        # check if this is the first encounter of min_path
                        """if min_path_length is None: 
                            min_path_length = len(path)"""

                        # we can double check len(path) == min_path_length before adding path
                        # but that wouldn't be needed if this implementation is correct
                        found_paths[key_for_value] = len(path) - 1 

                for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if 0 <= x2 < len(self.matrix[0]) and 0 <= y2 < len(self.matrix) and  self.matrix[y2][x2] != "#" and (x2, y2) not in seen:
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))
                        
            for j in range(len(nodes)):
                node = nodes[j][0]
                try:
                    value = found_paths[node]
                    if value != 0:
                        cost[j][i] = value
                except KeyError:
                    continue
        
        end = time.time()
        print(end - starttime)            
        return cost
            

    def create_adjacency_matrix(self):
        #cost = [[INF for column in range(len(self.list_of_nodes))]for row in range(len(self.list_of_nodes))]
        cost = [[0 for column in range(len(self.list_of_nodes))]for row in range(len(self.list_of_nodes))]
        p = Prims(len(self.list_of_nodes))
        nodes_by_index = list(self.list_of_nodes.items())
        p.graph = cost = self.bfs(nodes_by_index, cost)
        p.primMST()
        #self.kruskalMST(cost)

number_of_test_cases = int(input())

while number_of_test_cases > 0:
    sp = ShortestPath("S","A", "#", input())
    INF = float('inf')
    sp.create_map()
    V = len(sp.list_of_nodes)
    parent = [i for i in range(V)]
    sp.create_adjacency_matrix()

    number_of_test_cases -= 1