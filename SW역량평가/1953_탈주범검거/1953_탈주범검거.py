import sys
sys.stdin = open('input.txt')
"""
BFS로 풀어가면 될듯?
각 숫자에 맞게 방향 설정해서 퍼져나가게 해보자
"""
from collections import deque
"""
1: 상하좌우
2: 상하
3: 좌우
4: 상우
5: 하우
6: 하좌
7: 상좌
"""


def BFS(R, C, L):
    q = deque()
    q.append((R, C, 1)) # 좌표와 현재 시간
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    ans = 1

    while q:
        curr_r, curr_c, time = q.popleft()
        if time == L: # 지정된 시간에 도달했으므로 더 못감
            continue

        curr_p = board[curr_r][curr_c] # 현재 위치의 터널 종류 확인
        for k in pipe[curr_p]:
            nr, nc = curr_r + dr[k], curr_c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0 and not visited[nr][nc]:
                # 다음 위치의 터널 종류 확인
                next_p = board[nr][nc]
                # 연결 확인
                if opp[k] in pipe[next_p]:
                    # 즉, 내가 위로 가려는데 다음 파이르에 아래 방향 구멍이 뚫려 있다면
                    visited[nr][nc] = True
                    q.append((nr, nc, time + 1))
                    ans += 1
    return ans
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

pipe = {
    1: [0, 1, 2, 3], # 상 하 좌 우
    2: [0, 1], # 상 하
    3: [2, 3], # 좌 우
    4: [0, 3], # 상 우
    5: [1, 3], # 하 우
    6: [1, 2], # 하 좌
    7: [0, 2]  # 상 좌
}

opp = {0: 1, 1: 0, 2: 3, 3: 2} # 반대 방향 매칭 ( 상 <-> 하, 좌 <-> 우)

T = int(input())
for tc in range(1, T+1):
    # 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
    N, M, R, C, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{tc} {BFS(R, C, L)}")
