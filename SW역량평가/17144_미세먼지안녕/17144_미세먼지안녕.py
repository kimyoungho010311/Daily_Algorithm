import sys
sys.stdin = open('input.txt')
'''
미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
(r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.

공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# r 줄에 걸쳐 정보가 주어진다.
room = [list(map(int, input().split())) for _ in range(R)]
# 단순히 델타 탐색을 한번만 반복하면 먼지의 확산은 끝난다.

# 공기 청정기는 화살표에 따라서 미세먼지의 경로가 옮겨지는듯
# tmp 변수 생성해서 미세먼지 차례대로 옮길 때 공간 받아줘야 할 듯

# 공기청정기 위치 찾기 (항상 1열에 위치하며 두 행을 차지함)
air_purifier = []
for r in range(R):
    if room[r][0] == -1:
        air_purifier.append(r)

upper_ap = air_purifier[0]
lower_ap = air_purifier[1]


def clean_upper():
    # 위쪽 공청기 기준: 반시계 방향 순환
    # 서쪽 벽 (위에서 아래로)
    for r in range(upper_ap - 1, 0, -1):
        room[r][0] = room[r - 1][0]
    # 북쪽 벽 (오른쪽에서 왼쪽으로)
    for c in range(C - 1):
        room[0][c] = room[0][c + 1]
    # 동쪽 벽 (아래에서 위로)
    for r in range(upper_ap):
        room[r][C - 1] = room[r + 1][C - 1]
    # 남쪽 벽 (왼쪽에서 오른쪽으로)
    for c in range(C - 1, 1, -1):
        room[upper_ap][c] = room[upper_ap][c - 1]
    room[upper_ap][1] = 0

def clean_lower():
    # 아래쪽 공청기 기준: 시계 방향 순환
    # 서쪽 벽 (아래에서 위로)
    for r in range(lower_ap + 1, R - 1):
        room[r][0] = room[r + 1][0]
    # 남쪽 벽 (오른쪽에서 왼쪽으로)
    for c in range(C - 1):
        room[R - 1][c] = room[R - 1][c + 1]
    # 동쪽 벽 (위에서 아래로)
    for r in range(R - 1, lower_ap, -1):
        room[r][C - 1] = room[r - 1][C - 1]
    # 북쪽 벽 (왼쪽에서 오른쪽으로)
    for c in range(C - 1, 1, -1):
        room[lower_ap][c] = room[lower_ap][c - 1]
    room[lower_ap][1] = 0


for time in range(T):
    # 매 순간마다 완탐하는건 빠를 듯 최대 350번정도만 돌면 끝나니깐 시간 초과 안걸림
    add = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                spread = room[r][c] // 5
                check_count = 0
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        add[nr][nc] += spread
                        check_count += 1
                room[r][c] -= spread * check_count

    for r in range(R):
        for c in range(C):
            room[r][c] += add[r][c]

        # 2. 공기청정기 작동
        # 위쪽 (반시계방향)
        # 아래로 -> 오른쪽으로 -> 위로 -> 왼쪽으로 (값 당기기 방식이 구현하기 편함)


    clean_upper()
    clean_lower()

# 결과 출력 (공기청정기 -1 값 2개 제외)
ans = 0
for r in range(R):
    for c in range(C):
        if room[r][c] > 0: # 미세먼지(양수)일 때만 더하기
            ans += room[r][c]
print(ans)