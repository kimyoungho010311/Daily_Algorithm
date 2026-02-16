import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
# T = 1

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def search(i, j):
    q = deque([(i, j)])
    data[i][j] = 1

    while q:
        ci, cj = q.popleft()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < 100 and 0 <= nj < 100:

                if data[ni][nj] == 3:
                    return 1

                if data[ni][nj] == 0:
                    data[ni][nj] = 1
                    q.append((ni, nj))
    return 0

for tc in range(1, T+1):
    _ = int(input())
    data = [list(map(int, input().strip())) for _ in range(100)]

    result = search(1, 1)
    print(f"#{tc} {result}")