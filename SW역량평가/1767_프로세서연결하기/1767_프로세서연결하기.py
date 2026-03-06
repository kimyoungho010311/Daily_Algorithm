import sys
sys.stdin = open('input.txt')
from itertools import permutations, combinations
'''
N * N 개의 cell로 구성된 보드가 있다.

한개의 Cell은 Core / 전선이 가능하다.

가장자리에는 전원이 흐르고 있다.
Core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며, 전선끼리 교차는 불가능하다.

** 가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주한다.**

최대한 많은 Coreㅇ 전원을 연결하였을 경우 전선 길이의 합을 구한다.
단 전선의 길이가 최소가 되는 값을 구해라
'''
# 3시 30분에 문제 시작

# DFS로 벾가지 가는거 구현은 문제 없음
# 근데 어떤 Core부터 연결할지가 문제임

# 순열로 모든 경우의 수를 다 돌아봐야 하나?

# 일단 1차적으로 시작부터 전원이 들어온 Core는 경우의 수에서 제외해야함
# 순서가 정해진 걸로 순열 해본다음에
# 해당 경우의 수에서 연결 가능한 Core의 갯수를 구한다.
# 이러면 자동적으로 최소 비용이 나오나?

T = int(input())
T = 1
for tc in range(1, T+1):
    N = int(input())

    # 1: Core, 0: empty
    board = [list(map(int, input().split())) for _ in range(N)]

    count_cell = 0
    # {1: (0, 2), 2: (1, 2), 3: (2, 5), 4: (4, 0), 5: (4, 1), 6: (4, 3), 7: (5, 1)}
    all_cells_loc = {}

    # 주어진 보드 먼저 완탐 하면서
    # Cell의 갯수 위치를 찾아본다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count_cell += 1
                all_cells_loc[count_cell] = (i, j)

    # Cell이 벽에 붙어있는 경우는?
    # i = 0, N / j = 0, N 인 경우이다.
    cells_loc = {} # 전원이 안들어와있는 Cells
    already_on = 0

    for idx, coordi in enumerate(all_cells_loc.values()):
        i, j = coordi
        if i != 0 and i != N and j != 0 and j != N:
            cells_loc[idx]=(i, j)
        else:
            already_on += 1
    cells_comb = list(permutations(cells_loc.keys(), len(cells_loc.keys())))
    coordinate_cells = list(cells_loc.values()) # [(1, 2), (2, 5), (4, 1), (4, 3), (5, 1)]

    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # (1, 2, 4, 5, 6)
    for comb in cells_comb:
        # 매 순간마다 방문 기록을 초기화해야한다.
        # 일단 시간초과나면 백트래킹 ㄱㄱ
        visited = [[False] * N for _ in range(N)]

        # 생각해보면 DFS도 아닌듯? 그냥 4방향 일단 돌려보면서 최소값 찾는게 끝일거같다.
        for cell in comb:
            curr_i, curr_j = cells_loc[cell]
            # 시작 지점 방문 처리 한다음에
            visited[curr_i][curr_j] = True
            # 4방향을 각각 탐색하면서 최솟값 찾는다.
            # 만약 가는 방향에 cell or Ture값인 경우 continue 해서 다음 방향으로 간다.
            # 만약 해당 방향에서 벽까지 도착한다면 해당 전선으로 고정한다.
            for k in range(4):
                total_cost = 0
                result_cost = float('inf')
                while True:
                    next_i = curr_i + di[k]
                    next_j = curr_j + dj[k]
                    # 만약 다음지점에 cell이 존재 또는 방문(전선이 깔리면) 정지하고 다음 방향으로 돈다
                    if (next_i, next_j) in coordinate_cells or visited[next_i][next_j]:
                        break

                    # 만약 벽까지 도착한다면 최소값 비교해서 끝낸다.
                    if next_i == 0 or next_i == N or next_j == 0 or next_j == N:
                        if result_cost > total_cost:
                            result_cost = total_cost
                        break
                    print(total_cost)
                    total_cost += 1
                    visited[next_i][next_j] = True













