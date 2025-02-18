n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
block = []
answer = []

# Write your code here!
visited = [[False]*n for _ in range(n)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y):
    visited[x][y] = True
    count = 1

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and grid[nx][ny] == k:
                visited[nx][ny] = True
                count += dfs(nx, ny)
    return count

for i in range(n):
    for j in range(n):
        k = grid[i][j]
        num = dfs(i, j)
        block.append(num)
        if num >= 4:
            answer.append(num)

print(str(len(answer))+" "+str(max(block)))
