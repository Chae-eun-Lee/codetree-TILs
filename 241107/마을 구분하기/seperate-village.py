def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, grid, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    visited[x][y] = True
    s = 1
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
        
            if in_range(nx, ny, len(grid)) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))
                s += 1
    return s

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

count = 0
size = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            s = dfs(i, j, grid, visited)
            size.append(s)
            count += 1

print(count)
for s in sorted(size):
    print(s)