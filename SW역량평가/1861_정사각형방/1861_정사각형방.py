import sys
sys.stdin = open('input.txt')
"""
N*N 크기의 방이 있다.

각 방마다 1 <= x <= N^2의 숫자가 적혀 있으며 중복되는 숫자는 없다.

상하좌우로 이동이 가능하다.
현재 방보다 1이 더 커야하고 방 밖으로는 이동이 불가능하다.
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는지 구해라

=====================================
단순 BFS를 사용하면 시간초과가 날거같다.
백트래킹이나, 가지치기를 해서 연산량을 최대한 줄여줘야 겠다.

먼저 가지치기 방법부터 고민해본다.

다음 방으로 옮겨가기 위해선 정확히 1이 더 커야한다. 이걸 활용해서
if board[ci][cj] + 1 == board[ni][nj] 일때만 해당 방향으로 통해 BFS를 사용하도록 한다.

해당 방향이 아닐 경우 알고리즘의 끝에 방문처리를 취소한다.

max_depth, max_depth_start 가 있어야 한다.
BFS 알고리즘이 끝나는 순간 현재까지의 깊이를 max_depth와 비교하고 만약 가장 깊다면
max_depth_start 리스트에 추가한다.
"""
from collections import deque

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())


def BFS(si, sj):
    q = deque([(si, sj)])
    dist = 1  # 시작점 포함

    while q:
        r, c = q.popleft()  # i, j 대신 r, c 사용 권장 (반복문 변수와 안 겹치게)

        for k in range(4):
            ni, nj = r + di[k], c + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                # 다음 방이 현재 방보다 딱 1 클 때만 전진!
                if board[r][c] + 1 == board[ni][nj]:
                    q.append((ni, nj))
                    dist += 1
                    break  # 길이 하나뿐이라 찾으면 즉시 다음으로
    return dist


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_dist = 0
    start_num = float('inf')

    for i in range(N):
        for j in range(N):
            # 매번 해당 위치에서 갈 수 있는 끝까지 가보기
            res = BFS(i, j)

            if res > max_dist:
                max_dist = res
                start_num = board[i][j]
            elif res == max_dist:
                if board[i][j] < start_num:
                    start_num = board[i][j]

    print(f"#{tc} {start_num} {max_dist}")