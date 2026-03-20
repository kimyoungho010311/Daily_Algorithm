import sys
sys.stdin = open('input.txt')
# 북 동 남 서
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
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 주면 4방향에 청소가 필요한 공간이 있는지 확인한다.
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            has_empty = True # 만약 청소가 필요한 공간이 있으면 True로 바꾼 뒤 정지한다.
            break

    if not has_empty: # 주변에 청소되지 않은 빈 칸이 없는 경우
        # 바라보는 방향을 유지하며 후진
        back_d = (d + 2) % 4
        br, bc = r + dr[back_d], c + dc[back_d]

        # 후진 가능하면 이동
        if 0 <= br < N and 0 <= bc < M and room[br][bc] != 1:
            r, c = br, bc
        else: # 후진 불가능하면 멈춤
            break

    else: # 주변에 청소되지 않은 빈 칸이 있는 경우
        # 반시게방향 90도 회전
        d = (d - 1) % 4

        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc

print(cleaned_count)