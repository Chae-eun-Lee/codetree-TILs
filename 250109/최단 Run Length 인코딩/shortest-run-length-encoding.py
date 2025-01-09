A = list(input())
l = len(A)
answer = 20

def count_alpha(a):
    num = 2
    temp = 1
    for i in range(l-1):
        if a[i] == a[i+1]:
            temp += 1
        else:
            num += 2
            temp = 1
    if temp > 9:
        num += 1
    return num

for i in range(l):
    alpha = A.pop()
    A.insert(0, alpha)
    answer = min(answer, count_alpha(A))

print(answer)