import sys
sys.stdin = open('input.txt')
"""
N * N형태의 방
1 ~ N^2수가 있으며 숫자는 모두 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동이 가능하다.
물론 이동하려는 방이 존재해야하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커 야한다.
처음에 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성
"""
from collections import deque

def BFS(i, j):
    move_cnt = 1
    q = deque([(i, j, move_cnt)])
    visited[i][j] = True
    while q:
        curr_i, curr_j, move_cnt = q.popleft()

        for k in range(4):
            ni, nj = curr_i + di[k], curr_j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and room[curr_i][curr_j] + 1 == room[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj, move_cnt + 1))
    return move_cnt

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    room = []
    results = []
    max_move_cnt = -1

    for _ in range(N):
        tmp = list(map(int, input().split()))
        room.append(tmp)

    # 모든 원소를 순회하면서
    # BFS 알고리즘 적용하면 끝날거같은데..?

    for i in range(N):
        for j in range(N):
            visited = [[False] * N for _ in range(N)]

            move_cnt = BFS(i, j)

            if max_move_cnt < move_cnt:
                max_move_cnt = move_cnt
                results.append((room[i][j], max_move_cnt))
    results.sort(key=lambda x:x[1], reverse=True)
    print(f"#{tc} {results[0][0]} {results[0][1]}")