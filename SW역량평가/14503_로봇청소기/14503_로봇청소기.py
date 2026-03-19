import sys
sys.stdin = open('input.txt')
"""
로봇 청소기와 방의 상태가 주어질 때, 청소하는 영역의 개수를 구해라

방향은 동 서 남 북 중 하나이다.
긱 칸은 (r,c)로 나타낼 ㅅ ㅜ있고, 가작 북쪽 줄의 가장 서쪽 칸의 좌표가 (0, 0)
가장 남쪽 동쩍칸은 (N-1, M-1)이다.

즉, 좌표(r,c)는 북쪽에서 (r+1) 서쪽에서 (c+1)을 가리킨다.

1. 현재 칸을 청소
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    2-1. 바라보는 방향을 유지한 채로 한 칸 후지 ㄴ가능하면 한 칸 후진하고 1로 돌아간ㄷ.
    2-2. 뒤쪽 방향이 벽이면 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 잇는 경우
    3-1 반시계 방향으로 회전
    3-2. 바라보는 방향을 기준으로 앞쪽 ㅏㅋㄴ이청소 안되면 전진
    3-3. 1번으로 돌아감
"""

def check_clean_room(i, j):
    if room[i][j] == 0: # 0번이면 청소안한거이므로 청소로 변경한다.
        room[i][j] = 2
        visited[i][j] = True

#  그냥 단순히 DFS이지만 구현 난이도가 있는거같음

# 구현해야할 함수가 뭐가 있을까
# 함수까지 필요한가? 그냥 구현하면 될거같은데

# 1벽 0 빈공간, 2를 청소한 구역으로 선정한다.

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# N * M 방의 크기
N, M = map(int, input().split())

# 북 동 남 서
j, i, direction = map(int, input().split())
# 좌표값 계산하기 쉽게 이렇게 한다.
j -= 1
i -= 1

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# 1번 로직 구현
check_clean_room(i, j)
while True:
    check_direction = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        # 2번 로직
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and room[ni][nj] == 0:
            if direction == 0: direction = 3
            elif direction == 1: direction = 0
            elif direction == 2: direction = 1
            elif direction == 3: direction = 2
            i += di[direction]
            j += dj[direction]
            if room[i][j] == 0:
                check_clean_room(i, j)
        # 3번 로직
        elif 0 <= ni < N and 0 <= nj < M and visited[ni][nj] and room[ni][nj] == 2:
            check_direction += 1
    # 위에 반복문 나오면 4방향 모두 청소 안한곳이 없으니
    # 뒤로 뺴고 1로 돌아간다.
    # 뒤에 벽이면 여기서 break
    if check_direction == 4:
        i -= di[direction]
        j -= dj[direction]
        if 0 <= i < N and 0 <= j < M:
            if room[i][j] == 0:
                check_clean_room(i, j)
        else:
            break