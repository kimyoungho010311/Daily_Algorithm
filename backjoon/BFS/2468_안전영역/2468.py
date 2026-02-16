import sys
sys.stdin = open('input.txt')

from collections import deque
import copy

def BFS(mat, i, j):
    q = deque()
    q.append((i, j))
    mat[i][j] = 0 # 방문 처리를 하기 위해 0(물에 잠김) 처리를 한다.

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and mat[ni][nj] != 0:
                q.append((ni, nj))
                mat[ni][nj] = 0

N = int(input())  # 2 <= N <= 100
max_area = 0
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
# 최대 100*2 번의 최댓값을 찾기 위한 탐색을 해야함
# 높이는 1 이상 100 이하의 정수
# 최악: 1e6
"""
[6, 8, 2, 6, 2]
[3, 2, 3, 4, 6]
[6, 7, 3, 3, 2]
[7, 2, 5, 3, 6]
[8, 9, 5, 2, 7]
"""
mat_tmp = [list(map(int, input().split())) for _ in range(N)]

max_height = max(max(row) for row in mat_tmp)

for height in range(max_height+1):
    mat = copy.deepcopy(mat_tmp)
    rescue_are = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] <= height:
                mat[i][j] = 0 # 0을 물에 잠긴곳으로 처리한다.

    # 흠.. 2중 반목문을 두 번 쓰는게 별론데 합칠 방법을 모르겠음
    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0: # 0(잠긴곳)이 아니면 BFS를 시작한다.
                rescue_are += 1
                BFS(mat, i, j)

    # print(f"rescue: {rescue_are}")
    max_area = max(max_area, rescue_are)


print(max_area)