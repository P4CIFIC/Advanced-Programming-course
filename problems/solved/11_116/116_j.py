import sys
import time
from collections import defaultdict


class Graph:
    def __init__(self, vertices):

        self.V = vertices  # No. of vertices

        # dictionary containing adjacency List
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    # A recursive function used by shortestPath
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, stack)

        # Push current vertex to stack which stores topological sort
        stack.append(v)

    ''' The function to find shortest paths from given vertex.
        It uses recursive topologicalSortUtil() to get topological
        sorting of given graph.'''

    def shortestPath(self, s):

        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from source vertice
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)

        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float("Inf")] * (self.V)
        dist[s] = 0

        # Process vertices in topological order
        while stack:

            # Get the next vertex from topological order
            i = stack.pop()

            # Update distances of all adjacent vertices
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
        return dist


data = sys.stdin.read()
data = data.replace('\n', ' ')
data = data.split()

rows, cols = 0, 0
lines = 0
matrix = []
graph = []
while True:
    # print(time.perf_counter())
    if rows == 0:
        rows = int(data[lines])
        cols = int(data[lines + 1])
        lines += 2
    for j in range(rows):
        matrix.append([])
        for k in range(cols):
            matrix[j].append(data[lines])
            lines += 1
    for x in matrix:
        x.reverse()
    matrix.insert(0, matrix[len(matrix) - 1])
    matrix.append(matrix[1])

    for i in range(cols - 1):
        for j in range(1, rows + 1):
            u = rows * i + j
            v = u + rows
            graph.append([u, v, int(matrix[j][i + 1])])
            if j == 1:
                v = rows * (i + 2)
            else:
                v = v - 1
            graph.append([u, v, int(matrix[j - 1][i + 1])])
            if j == rows:
                v = u + 1
            else:
                v = u + rows + 1
            graph.append([u, v, int(matrix[j + 1][i + 1])])
    for i in range(1, rows + 1):
        graph.insert(0, [0, i, int(matrix[i][0])])
    g = Graph(rows * cols + 1)
    for x in graph:
        g.addEdge(x[0], x[1], x[2])
    # print(time.perf_counter())
    dist = g.shortestPath(0)
    # print(time.perf_counter())

    dist.pop(0)
    dist = list(zip(*[dist[i::rows] for i in range(rows)]))
    path = []
    c = dist.pop()
    min_step = min(c)
    index_min = min(range(len(c)), key=c.__getitem__)
    path.append(index_min + 1)
    for c in dist[::-1]:
        c = list(c)
        prev_path_col = path[len(path) - 1]
        step_up = prev_path_col + 1
        if prev_path_col + 1 > rows:
            step_up = 1
        step_down = prev_path_col - 1
        if prev_path_col - 1 == 0:
            step_down = rows
        for i in range(len(c)):
            if i + 1 != prev_path_col and i + 1 != step_up and i + 1 != step_down:
                c[i] += 99999999999
        index_min = min(range(len(c)), key=c.__getitem__)
        path.append(index_min + 1)
    # print(time.perf_counter())
    print(*path)
    print(min_step)

    rows, cols = 0, 0
    matrix = []
    graph = []
    if lines == len(data):
        break