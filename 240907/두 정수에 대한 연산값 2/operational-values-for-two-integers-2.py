a, b = map(int, input().split())
def cal(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        a*=2
        b+=10
    return a, b
print(cal(a, b)[0], cal(a, b)[1])