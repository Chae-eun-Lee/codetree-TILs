n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

for i in range(n):
    for j in range(m-2):
        case1 = 0
        for k in range(3):
            case1 += grid[i][j+k]
        max_num = max(max_num, case1)
    
for i in range(n-2):
    for j in range(m):
        case2 = 0
        for k in range(3):
            case2 += grid[i+k][j]
        max_num = max(max_num, case2)

case3 = []
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            case3.append(grid[i][j]+grid[i-1][j]+grid[i][j-1])
        if i > 0 and j < (m-1):
            case3.append(grid[i][j]+grid[i-1][j]+grid[i][j+1])
        if i < (n-1) and j > 0:
            case3.append(grid[i][j]+grid[i+1][j]+grid[i][j-1])
        if i < (n-1) and j < (m-1):
            case3.append(grid[i][j]+grid[i+1][j]+grid[i][j+1])

case4 = max(case3)

print(max(case4, max_num))