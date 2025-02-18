import sys
sys.setrecursionlimit(10**6)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_area = []


def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] > k

def dfs(x, y):
    visited[x][y] = True
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


max_height = max(map(max, grid))
for k in range(1, max_height+1):
    total = 0
    visited = [([False]*m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if can_go(i, j):
                total += 1
                dfs(i, j)
    max_area.append([total, k])

max_area.sort(key=lambda x:(x[0], -x[1]), reverse=True)
print(str(max_area[0][1])+" "+str(max_area[0][0]))



