n, m = map(int, input().split())
ary = [n*(x+1) for x in range(m)]
for i in range(m):
    if m*(i+1) in ary:
        print(m*(i+1))
        break