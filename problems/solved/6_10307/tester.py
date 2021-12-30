import heapq

directions = {'LEFT':(0, -1), 'RIGHT':(0,1), 'UP':(-1, 0), 'DOWN':(1, 0)}

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

lines = [line.rstrip('\n') for line in open('borgmazetestcases.txt')]
weights = 0
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

lines = []

    edges = []
    temp2 = aliens[:]
    while(len(aliens) > 1):
        temp = aliens[:1][0]
        aliens = aliens[1:]
        dist = dijkstra(temp, aliens, visited)
        for alien in aliens:
            edges.append([temp, dist[alien], alien])

    hello = createMST(edges, temp2, len(temp2))
    #
    print(sum(hello))
    
