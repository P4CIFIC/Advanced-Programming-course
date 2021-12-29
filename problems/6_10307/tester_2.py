import heapq, sys

directions = {'LEFT':(0, -1), 'RIGHT':(0,1), 'UP':(-1, 0), 'DOWN':(1, 0)}

class Vertices:
    def __init__(self):
        self.vertices = list()

    def printAll(self):
        for vertice in self.vertices:
            print(vertice)

    def addVertices(self, i, j):
        self.vertices.append((i, j))

    def length(self):
        return len(self.vertices)

    def find(self, i, j):
        if (i, j) in self.vertices:
            return True
        return False

    def getVertices(self):
        return self.vertices

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = {}

    def addEdge(self,f,t, t1, w):
        if f not in self.graph:
            self.graph[f] = []
        self.graph[f].append((t, t1, w))

    def getEdges(self):
        return self.graph

    def getEdgesById(self, id):
        return self.graph[id]

class UnionFind:
    def __init__(self):
        self.nodeMap = {}

    def getKeys(self):
        return list(self.nodeMap.keys())

class Node:
    def __init__(self, data, rank):
        self.data = data
        self.parent = 0
        self.rank = rank

def traverseMaze(x, y, visited, aliens, start, lineCount):
    alientCount = 1
    for i in range(y):
        temp = list(lines[lineCount])
        for j in range(len(temp)):
            if(temp[j] == '#'):
                visited[i][j] = True
            if(temp[j] == 'S'):
                start = (i, j)
            if(temp[j] == 'A'):
                aliens.append((i, j))
                alientCount += 1
        lineCount += 1
    return aliens, start, lineCount, visited

def makeSet(data, rank, UnionFind):
    node = Node(data, rank)
    node.parent = node
    UnionFind.nodeMap[data] = node

def union(UnionFind, data1, data2):
    node1 = UnionFind.nodeMap[data1]
    node2 = UnionFind.nodeMap[data2]
    parent1 = findset(node1)
    parent2 = findset(node2)


    if(parent1.rank >= parent2.rank):
        if(parent1.rank == parent2.rank):
            parent1.rank += 1
            parent2.parent = parent1

        parent2.parent = parent1
    else:
        parent1.parent = parent2

def findset(node):
    node_parent = node.parent
    if(node == node_parent):
        return node_parent
    node_parent = findset(node_parent.parent)
    node.parent = node_parent
    return node_parent

def createMST(edges, temp, sizeofnodes):
    mst = []
    uf = UnionFind()
    for edge in temp:
        makeSet(edge, 0, uf)

    sortedEdges = sorted(edges, key= lambda item: item[1])
    for edge in sortedEdges:
        if not findset(uf.nodeMap[edge[0]]) == findset(uf.nodeMap[edge[2]]):
            union(uf, edge[0], edge[2])
            mst.append(edge[1])
            if(len(mst) == sizeofnodes - 1):
                break
    return mst

lines = [line.rstrip('\n') for line in open(r"C:\Users\malek\Desktop\Advanced-Programming-Assignments\problems\6_10307\borgmazetestcases.txt")]
#lines = [line.rstrip('\n') for line in sys.stdin]
weights = 0
testcases = int(lines[0])
lineCount = 1
alientCount = 1

def dijkstra(source, vertices, visited):
    temp = [row[:] for row in visited]

    INF = 9999
    dist = {x: INF for x in vertices}
    dist[source] = 0
    PQ = []
    row = 0
    col = 0

    heapq.heappush(PQ, [dist[source], source])

    while(PQ):
        u = heapq.heappop(PQ)
        u_dist = u[0]
        u_id = u[1]
        if u_dist == dist[u_id]:
            temp[u_id[0]][u_id[1]] = True
            for direct in directions.values():
                row = u_id[0] + direct[0]
                col = u_id[1] + direct[1]
                if(not temp[row][col]):
                    newNode = (row, col)
                    dist[newNode] = u_dist + 1
                    temp[row][col] = True
                    heapq.heappush(PQ, [dist[newNode], newNode])
    return dist

for i in range(testcases):
    data = list(map(int, lines[lineCount].split()))
    x = data[0]
    y = data[1]
    aliens = []
    start = 0
    graph = 0
    visited = [[False for i in range(x)] for j in range(y)]
    lineCount += 1

    aliens, start, lineCount, visited = traverseMaze(x, y, visited, aliens, start, lineCount)
    aliens.insert(0, start)

    if(start == 0 or len(aliens) == 1):
        print("0")
        continue

    edges = []
    temp2 = aliens[:]
    while(len(aliens) > 1):
        temp = aliens[:1][0]
        aliens = aliens[1:]
        dist = dijkstra(temp, aliens, visited)
        for alien in aliens:
            edges.append([temp, dist[alien], alien])
    print(sum(createMST(edges, temp2, len(temp2))))