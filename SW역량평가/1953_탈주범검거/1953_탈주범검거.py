import sys
sys.stdin = open('input.txt')
"""
BFS로 풀어가면 될듯?
각 숫자에 맞게 방향 설정해서 퍼져나가게 해보자
"""
from collections import deque
T = int(input())
"""
1: 상하좌우
2: 상하
3: 좌우
4: 상우
5: 하우
6: 하좌
7: 상좌
"""
def BFS(R, C, board, visited):
    q = deque()
    q.append((R, C))
    visited[R][C] = True

    while q:
        curr_i, curr_j = q.popleft()
        # 현재 위치의 값에 따라서 상하좌우 어디로 나갈지 정한다.
        if board[curr_i][curr_j] == 1:
            for k in range(4):
                ni = curr_i + di[k]
                nj = curr_j + dj[k]

                if 0 <= N < ni and 0 <= M < nj and board[ni][nj] != 0 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj))



# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = 1
for tc in range(1, T+1):
    # 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
    N, M, R, C, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    BFS(R, C, board, visited)