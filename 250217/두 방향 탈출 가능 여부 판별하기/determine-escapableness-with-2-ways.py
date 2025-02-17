n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

order = 0
visited = [([0]*m) for _ in range(n)]
answer = [([0]*m) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < m and 0<=y<n 

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

# Write your code here!
def dfs(x, y):
    global order

    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            answer[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

answer[0][0] = order
order += 1
visited[0][0] = 1
dfs(0, 0)

if answer[n-1][-1] == 0:
    print(0)
else:
    print(1)