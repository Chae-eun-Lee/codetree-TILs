n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

for i in range(e1-s1+1):
    blocks.pop(s1-1)
for j in range(e2-s2+1):
    blocks.pop(s2-1)

l = len(blocks)
if l == 0:
    print(0)
else:
    print(l)
    for k in range(l):
        print(blocks[k])
