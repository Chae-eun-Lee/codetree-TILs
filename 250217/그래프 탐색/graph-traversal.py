from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)


def dfs(vertex):
    count = 1
    for cur in graph[vertex]:
        if not visited[cur]:
            visited[cur] = True
            count += dfs(cur)
    return count

print(dfs(1)-2)