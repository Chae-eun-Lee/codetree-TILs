n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_gold = 0

def get_num(row, column):
    num_gold = 0
    for r in range(row, row+3):
        for c in range(column, column+3):
            num_gold += grid[r][c]
    
    return num_gold

for i in range(n-2):
    for j in range(n-2):
        num_gold = get_num(i, j)
        max_gold = max(max_gold, num_gold)

print(max_gold)

