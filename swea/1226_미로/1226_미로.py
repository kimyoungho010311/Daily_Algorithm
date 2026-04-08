import sys
sys.stdin = open('input.txt')

'''
BFS 로 풀어야함
마지막에 도달한 위치가 3이 아니면 0 3이 맞으면 1출력한다
'''
from collections import deque

T = 10

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = True

    while q:
        ci, cj = q.popleft()

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if 0 <= ni < 16 and 0 <= nj < 16 and not visited[ni][nj]:
                if board[ni][nj] == 3:
                    return 1
                if board[ni][nj] == 0:
                    visited[ni][nj] = True
                    q.append((ni, nj))

    return 0

for tc in range(1, T+1):
    int(input())

    board = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    
    # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                si, sj = i, j
                break

    print(f"#{tc} {BFS(si, sj)}")
