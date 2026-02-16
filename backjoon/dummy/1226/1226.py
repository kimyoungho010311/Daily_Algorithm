"""
16 * 16 행렬이 주어지고
시작점은 (1, 1) 도착지점은 (13, 13)이다.
0인 지점만 움직일 수 있다.
시작부터 끝까지 도달 가능하면 1, 불가능 하면 0을 출력한다.
"""
import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
# T = 1

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def search(start_i, start_j):
    q = deque([(start_i, start_j)])
    mat[start_i][start_j] == 1

    while q:
        ci, cj = q.popleft()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < 16 and 0 <= nj < 16:

                if mat[ni][nj] == 3:
                    return 1

                if mat[ni][nj] == 0:
                    mat[ni][nj] = 1
                    q.append((ni, nj))
    return 0

for tc in range(1, T+1):
    _ = int(input())
    mat = [list(map(int, input().strip())) for _ in range(16)]

    print(f"#{tc} {search(1, 1)}")