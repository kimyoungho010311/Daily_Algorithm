import sys
sys.stdin = open('input.txt')

"""
[로봇 청소기 의사코드 (Logic Flow)]

1. 방향 정의: 0:북, 1:동, 2:남, 3:서 순서로 이동 벡터(dr, dc)를 만든다.
2. 입력 받기: 지도의 크기, 로봇의 위치와 방향, 지도의 상태(0:빈칸, 1:벽)를 저장한다.
3. 청소 시작 (무한 루프):
    STEP A. 현재 칸이 청소되지 않았다면(0), 청소하고(2) 카운트를 올린다.
    STEP B. 주변 4칸을 탐색해서 '청소되지 않은 빈칸(0)'이 있는지 확인한다.

    STEP C-1. [빈칸이 없는 경우]
        - 바라보는 방향을 유지한 채로 '후진'할 좌표를 계산한다.
        - 뒤가 벽(1)이 아니라면 후진해서 STEP A로 돌아간다.
        - 뒤가 벽(1)이라서 후진도 못 하면 작동을 멈춘다(Break).

    STEP C-2. [빈칸이 있는 경우]
        - 반시계 방향으로 90도 먼저 회전한다. (d = (d-1)%4)
        - 내 바로 앞칸이 청소되지 않은 빈칸(0)이라면 한 칸 전진한다.
        - STEP A로 돌아간다.
"""
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cleaned_count = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned_count += 1

    has_empty = False
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            has_empty = True
            break
    if not has_empty:
        back_d = (d + 2) % 4
        br, bc = r + dr[back_d], c + dc[back_d]

        if 0 <= br < N and 0 <= bc < M and room[br][bc] != 1:
            r, c = br, bc
        else:
            break
    else:
        d = (d - 1) % 4
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0
            r, c = nr, nc

print(cleaned_count)