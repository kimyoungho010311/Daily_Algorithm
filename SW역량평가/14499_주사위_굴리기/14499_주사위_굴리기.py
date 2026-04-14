import sys
sys.stdin = open('input.txt')
"""
크기가 M * M인 지도가 존재한다.
오른쪽 동쪽, 위쪽 북쪽이다.

주사위 기준 윗면이 1이고, 동쪽은 3 놓여져 있는 곳의 좌표는 (x, y)이다. 가장 처음 추사위에는 모든 면에 0이 적혀있다.

지도의 각 칸에는 정수가 하나씩 쓰여있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수의 칸에 복사된다.
(아마도 그러면 1의 반대방향 6이 적힌다는 예시인듯)

0이 아닌 경우에는 지도에 있는 정수가 주사위의 바닥 면에 복사되고 지도의 숫자는 0으로 변한다.

주사위는 지도안에만 존재한다.
만약 밖으로 이동하려고 하면 해당 명령은 무시하며, 출력도 하면 안된다. *****

그냥 간단한 시뮬레이션같다. 구현도 필요없을거같은데
주사위의 정보는 2차원 리스트로 구현한 다음에 6개의 리스트만 채워넣으면 끝날 듯

[0, 2, 0]
[4, 1, 3]
[0, 5, 0]
[0, 6, 0]
이런 느낌으로... 다뤄야 할 듯 그리고 바닥면 고를 때에는 % 써가지고 가로면 +2 세로면 +2 해야 할듯

출력으로는 윗면의 값만 출력하고 주사위가 맵 밖으로 나갈려고 하면 그냥 continue 해야한다.
=====================================

주사위를 2차원 배열로 다루는게 아니라 일차원 리스트로 다루고 각 원소끼리 스왑하면 끝날거같은데 
머리속으로는 어케 해야할지 모르겠음.. 그림그려야할듯 수고링
"""
N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 명령 정보 (1: 동, 2: 서, 3: 북, 4: 남)
orders = list(map(int, input().split()))

# 주사위 초기화
# [0, 윗, 북, 동, 서, 남, 바닥]
dice = [0] * 7

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

curr_x, curr_y = x, y

for move in orders:

    nx = curr_x + dx[move]
    ny = curr_y + dy[move]

    # 지도를 벗어나는지 체크
    if not(0 <= nx < N and 0 <= ny < M):
        continue

    # 주사위 굴리기
    # dice[1]: 상, [2]: 북, [3]: 동, [4]: 서, [5]: 남, [6]: 하
    if move == 1: # 동쪽
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    if move == 2: # 서쪽
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    if move == 3: # 북쪽
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    if move == 4: # 남쪽
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

    # 주사위 바닥과 지도 값 교환
    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        # 칸이 0이 아니면 칸의 수가 주사위 바닥면으로 복사되고, 칸은 0이 된다.
        dice[6] = board[nx][ny]
        board[nx][ny] = 0

    # 좌표 업데이트, 출력
    curr_x, curr_y = nx, ny
    print(dice[1])