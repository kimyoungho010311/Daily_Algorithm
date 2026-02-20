import sys
sys.stdin = open('input.txt')
"""
바이러스가 퍼지지 않게 벽을 세워야 한다.

연구소: N * M의 직사각형
직사각형은 1*1크기로 이루어짐
연구소는 빈 칸, 벽으로 이루어짐, 벽은 칸 하나를 가득 차지

벽을 3개 세운 뒤 바이러스가 퍼질 수 없는 곳을 안전 영역이라 한다.
연구소 지도가 주어질 때 가장 큰 안전영역 크기의 최댓값을 구해라
"""
from itertools import combinations
# 여기 아래에 코드 ㄱㄱ

def DFS(curr_i, curr_j):
    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 각 바이러스의 위치마다 실행해야 한다.
    for k in range(4):
        ni, nj = curr_i + di[k], curr_j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and tmp_mat[ni][nj] == 0:
                tmp_mat[ni][nj] = 2 # 바이러스 전염
                DFS(ni, nj) # 다음칸으로 재귀 호출

# 세로, 가로
N, M = map(int, input().split())

# 0: 빈칸
# 1: 벽
# 2: 바이러스
mat = [list(map(int, input().split())) for _ in range(N)]

# 모든 경우의 수를 다 해봐야 한다.
# 최대 크기는 8 * 8이니깐 해볼만함

# 1. 지도에서 0을 모두 뽑아 벽짓기 후보 combination을 만들고, 후보에 벽을 짓는다.

max_safe_area = -1
candidate_wall = []
virus = []
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0: # 해당 값이 0이면 벽짓기 후보에 추가한다.
            candidate_wall.append((i, j))
        elif mat[i][j] == 2:
            # 바이러스의 위치
            virus.append((i, j))

# [((0, 1), (0, 2), (0, 3)), ((0, 1), (0, 2), (0, 6)), ((0, 1), (0, 2),...
for comb in combinations(candidate_wall, 3):
    # 임시적으로 원본 배열을 복사해주고 복사본에 시뮬레이션한다.
    tmp_mat = [row[:] for row in mat]
    # 벽 세우기
    for idx in range(len(comb)):
        i, j = comb[idx][0], comb[idx][1]
        tmp_mat[i][j] = 1
    # 2. 각 경우의 수마다 바이러스를 퍼트린다. DFS
    for v_i, v_j in virus:
        DFS(v_i, v_j)
    # 3. 마지막에 0이 남아 있는 갯수를 카운팅
    safe_area = sum(row.count(0) for row in tmp_mat)

    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)