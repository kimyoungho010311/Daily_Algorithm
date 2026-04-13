import sys
sys.stdin = open('input.txt')

"""
N*N크기의 미로, 출발지, 목적지가 주어진다.
이 때 최소 몇 개의 칸을 지나야 목적지에 도달하는지 출력한다.

만약 경로가 없으면 0을 출력한다.

뭐여.. 최종 결과에서 1 빼야하는겨?


"""

from collections import deque

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(ci, cj):
    q = deque([(si, sj, 0)])
    visited[si][sj] = True

    while q:
        ci, cj, curr_result = q.popleft()

        if board[ci][cj] == 3:
            return curr_result - 1

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 1 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj, curr_result + 1))
    return 0

T = int(input())
for tc in range(1, T+1):
    # 미로 크기
    N = int(input())

    board = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                si, sj = i, j
    print(f"#{tc}", BFS(si, sj))
