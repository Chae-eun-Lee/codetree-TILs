n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
happy = 0

for i in range(n):
    keep = 1
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
            keep += 1
        else:
            keep = 1

        if keep >= m:
            happy += 1
            break

for i in range(n):
    keep = 1
    for k in range(n-1):
        if grid[k][i] == grid[k+1][i]:
            keep += 1
        else:
            keep = 1
        
        if keep >= m:
            happy += 1
            break

print(happy)