import sys, heapq

class Prims():
    
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.graph = 0

    def get_mst_distance(self, parent):
        sum = 0
        for i in range(1, self.vertices_count):
            sum+=self.graph[i][parent[i]]
        print(sum)

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.vertices_count):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def solve(self):
        key = [sys.maxsize] * self.vertices_count
        parent = [None] * self.vertices_count
        if self.vertices_count < 1:
            return
        key[0] = 0
        mstSet = [False] * self.vertices_count
        parent[0] = -1

        for cout in range(self.vertices_count):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.vertices_count):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.get_mst_distance(parent)

def dijkstra(source_node, vertices, visited):
    directions = [(0, -1), (0,1), (-1, 0),(1, 0)]
    INF = float('inf')
    visited_copy = [i[:] for i in visited]
    distance = {i: INF for i in vertices}
    distance[source_node] = 0
    priority_queue = []
    row = 0
    column = 0
    heapq.heappush(priority_queue, [distance[source_node], source_node])
    
    while(priority_queue):
        element = heapq.heappop(priority_queue)
        element_distance = element[0]
        element_position = element[1]
        if element_distance == distance[element_position]:
            visited_copy[element_position[0]][element_position[1]] = True
            for direction in directions:
                row = element_position[0] + direction[0]
                column = element_position[1] + direction[1]
                if not visited_copy[row][column]:
                    node = (row,column)
                    distance[node] = element_distance + 1
                    visited_copy[row][column] = True
                    heapq.heappush(priority_queue, [distance[node], node])
    return distance

def explore_maze(case, width, height):
    visited = [[False for i in range(width)] for j in range(height)]
    aliens = []
    start = 0
    for i in range(height):
        line = case[i]
        for j in range(len(line)):
            char = line[j]
            if char == "#":
                visited[i][j] = True
            elif char == "A":
                aliens.append((i,j))
            elif char == "S":
                start = (i,j)
    aliens.insert(0, start)
    return start, aliens, visited
        
def read_input(test_case_counter):
    lines = {}
    counter = 0
    while counter < test_case_counter:
        test_case = []
        dimensions = [int(element) for element in input().split()]
        for i in range(dimensions[1]):
            test_case.append(input())
        test_case.insert(0, dimensions)
        lines[counter] = test_case
        counter += 1
    return lines

number_of_cases = int(input())
cases = read_input(number_of_cases)
for i in range(number_of_cases):
    case = cases.get(i)
    dimensions = case.pop(0)
    width = dimensions[0]
    height = dimensions[1]
    start, aliens, visited = explore_maze(case, width, height)
    if start == 0 or len(aliens) == 1:
        print("0")
        continue
    
    weighted_edges = []
    all_aliens = aliens[:]
    while len(aliens) > 1:
        source = aliens[:1][0]
        aliens = aliens[1:]
        distance = dijkstra(source, aliens, visited)
        for alien in aliens:
            weighted_edges.append([source, distance[alien], alien])
    
    cost = [[0 for i in range(len(all_aliens))]for j in range(len(all_aliens))]
    for edge in weighted_edges:
        column = all_aliens.index(edge[0])
        weight = edge[1]
        row = all_aliens.index(edge[2])
        cost[row][column] = weight
        cost[column][row] = weight
    p = Prims(len(all_aliens))
    p.graph = cost
    p.solve()