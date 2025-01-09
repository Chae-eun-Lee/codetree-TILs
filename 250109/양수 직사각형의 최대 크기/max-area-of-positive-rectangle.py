n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 사각형 크기 얼마나 좁힐자
for height in range(n, 0, -1):
    for width in range(m, 0, -1):
        # 사각형 반복되는 개수
        for k in range(n - height + 1):
            for l in range(m - width + 1):
                valid = True
                #사각형 내부 양수 검사
                for a in range(k, height+k):
                    for b in range(l, width+l):
                        if grid[a][b] < 1:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    answer = max(answer, height*width)
print(answer)