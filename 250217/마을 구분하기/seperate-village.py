n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
total = 0
people = []

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def dfs(x, y):
    visited[x][y] = True
    person = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        ndx, ndy = x+dx, y+dy

        if can_go(ndx, ndy):
            visited[ndx][ndy] = True
            person += dfs(ndx, ndy)
    return person

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            people.append(dfs(i, j))
            total += 1

print(total)
people.sort()
for p in people:
    print(p)

