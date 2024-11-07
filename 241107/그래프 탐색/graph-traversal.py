n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)

def dfs(graph, vertex):
    visited[vertex] = True
    count = 1
    for c in graph[vertex]:
        if not visited[c]:
            count += dfs(graph, c)

    return count
print(dfs(graph, 1)-1)