a, b = map(int, input().split())
def cal(a, b):
    c = min(a, b)
    d = max(a, b)
    c += 10
    d *= 2
    return c, d
print(cal(a, b)[0], cal(a, b)[1])