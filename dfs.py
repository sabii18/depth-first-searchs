from collections import defaultdict

def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)
    return path

graph = defaultdict(list)
n, e = map(int, input("Enter number of vertices and edges: ").split())

for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)  

start = 'A'
visited = defaultdict(bool)
path = []

traversedpath = dfs(graph, start, visited, path)
print("\nDFS Traversal Path:", traversedpath)
