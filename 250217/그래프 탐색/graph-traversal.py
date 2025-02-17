from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False]*(n+1)
answer = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)


def dfs(vertex):
    global answer
    for cur in graph[vertex]:
        if not visited[cur]:
            visited[cur] = True
            answer += 1
            dfs(cur)

visited[1] = True
dfs(1)
print(answer)