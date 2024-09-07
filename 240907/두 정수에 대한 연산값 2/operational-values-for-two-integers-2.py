a, b = map(int, input().split())
def cal(a, b):
    c = min(a, b)
    d = max(a, b)
    a = c+10
    b = d*2
    return a, b
print(cal(a, b)[0], cal(a, b)[1])