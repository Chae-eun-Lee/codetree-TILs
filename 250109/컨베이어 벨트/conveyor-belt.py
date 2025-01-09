n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(t%(n*2)):
    temp1 = u[-1]
    temp2 = d[-1]
    for j in range(n-1, 0, -1):
        u[j] = u[j-1]
        d[j] = d[j-1]
    u[0] = temp2
    d[0] = temp1

print(*u)
print(*d)