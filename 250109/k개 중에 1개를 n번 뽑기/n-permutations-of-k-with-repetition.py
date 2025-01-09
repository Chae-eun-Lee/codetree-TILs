K, N = map(int, input().split())
answer = []

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(num):
    if num == N+1:
        print_ans()
        return
    for i in range(K):
        answer.append(i+1)
        choose(num+1)
        answer.pop()
    return

choose(1)