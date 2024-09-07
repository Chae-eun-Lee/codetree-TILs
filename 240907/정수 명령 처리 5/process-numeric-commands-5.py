ary = []
n = int(input())
for _ in range(n):
    ip = list(input().split())
    if ip[0] == 'push_back':
        ary.append(ip[1])
    elif ip[0] == 'pop_back':
        ary.pop()
    elif ip[0] == 'size':
        print(len(ary))
    else:
        k = int(ip[1]) - 1
        print(ary[k])