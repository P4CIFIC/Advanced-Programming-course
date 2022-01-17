# Using a Python dictionary to act as an adjacency list
G = {
    'A' : [('B', 2),('C',4)],
    'B' : [('D',3), ('E', 5)],
    'C' : [('F', 7)],
    'D' : [],
    'E' : [('F', 9)],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

"""def dfs(visited, graph, node):
    if node[0] not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour[1] < 9:
                dfs(visited, graph, neighbour[0])"""

e = 5

visited = set() # Set to keep track of visited nodes.

def dfs(visited, G, node, node_weight, counter):
    if node not in visited and node_weight < e:
        counter = counter + 1
        visited.add(node)
        for neighbour in G[node]:
            counter = dfs(visited, G, neighbour[0], neighbour[1], counter)
    return counter

counter = 0
counter = dfs(visited, G, 'A', 0, counter)
if counter == len(G):
    print("Not in MST")
else:
    print("In MST")