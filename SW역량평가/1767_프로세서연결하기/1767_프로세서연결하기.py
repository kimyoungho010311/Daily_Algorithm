import sys
sys.stdin = open('input.txt')
'''
N * N 개의 cell로 구성된 보드가 있다.

한개의 Cell은 Core / 전선이 가능하다.

가장자리에는 전원이 흐르고 있다.
Core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며, 전선끼리 교차는 불가능하다.

** 가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주한다.**

최대한 많은 Coreㅇ 전원을 연결하였을 경우 전선 길이의 합을 구한다.
단 전선의 길이가 최소가 되는 값을 구해라
'''
def is_available(i, j, k, N, board):
    # 해당 방향으로 끝까지 가능한가?
    curr_i, curr_j = i + di[k], j + dj[k]
    while 0 <= curr_i < N and 0 <= curr_j < N:
        # 가는길에 전선 코어 있으면 실패
        if board[curr_i][curr_j] != 0:
            return  False
        curr_i += di[k]
        curr_j += dj[k]
    return True

def set_wire(i, j, k, N, board, value):
    # 전선을 깔거나 다시 지우는 함수
    # 연결된 전선의 길이를 반환
    count = 0
    curr_i, curr_j = i + di[k], j + dj[k]
    while 0 <= curr_i < N and 0 <= curr_j < N:
        board[curr_i][curr_j] = value
        curr_i += di[k]
        curr_j += dj[k]
        count += 1
    return  count

def dfs(idx, core_cnt, wire_len):
    global  max_cores, min_wire_len

    # 남은 코어를 다 연결해도 현재 찾아둔 코어 수보다 작다면 자른다.
    if core_cnt + (len(cores) - idx) < max_cores:
        return

    # 모든 코어를 다 확인했을 때
    if idx == len(cores):
        # 코어를 더 많이 연결한 경우
        if core_cnt > max_cores:
            max_cores = core_cnt
            min_wire_len = wire_len
        # 코어수는 같은데 전선 길이가 더 짧은 경우
        elif core_cnt == max_cores:
            min_wire_len = min(min_wire_len, wire_len)
        return

    i, j = cores[idx]

    for k in range(4):
        if is_available(i, j, k, N, board):
            # 전선 깔기 (전선은 2로 취급)
            added_len = set_wire(i, j, k, N, board, 2)
            # 다음 코어로 이동
            dfs(idx + 1, core_cnt + 1, wire_len + added_len)
            # 백트래킹: 전선 다시 치우기
            set_wire(i, j, k, N, board, 0)
    dfs(idx + 1, core_cnt, wire_len)

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    max_cores = 0
    min_wire_len = float('inf')

    # 가장 자리를 제외한 코어 찾기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    continue
                cores.append((i, j))
    # 검사할 코어 인덱스, 연결된 코어 수, 누적 전선 길이
    dfs(0, 0, 0)

    print(f"#{tc} {min_wire_len}")