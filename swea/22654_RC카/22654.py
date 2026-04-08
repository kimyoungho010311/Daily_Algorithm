import sys
sys.stdin = open('input.txt')

"""
'G' : RC카가 이동 가능한 땅
'T' : RC카가 이동이 불가능한 나무
'X' : 현재 RC카의 위치
'Y' : RC카를 이동 시키고자 하는 위치
'A' : 앞으로 이동 - 나무가 있는 곳이나 필드를 벗어나는 경우에는 아무 일도 일어나지 않는다.
'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

모든 커맨드가 종료되었을 때 목적지에 도달 했는지 출력해라
"""

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    # 필드의 크기
    N = int(input())

    board = [list(map(str, input().strip())) for _ in range(N)]

    # 조종 횟수
    Q = int(input())
    orders = [list(map(str, input().split())) for _ in range(Q)]

    for i in range(Q):
        orders[i][0] = int(orders[i][0]) # [[7, 'RRAALAA'], [8, 'RRAALAAA'], [12, 'RAARRALAALAA']]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                si, sj = i, j
                break

    result = []

    for order in orders:
        order_len = order[0]
        diractions = order[1]
        dir = 0 # 일단 시작은 항상 위에 바라보고 있음
        ci, cj = si, sj
        # (dir + 1) % 4
        for idx in range(order_len):
            if diractions[idx] == 'A':
                # 다음 위치를 구한다음에
                # 만약 다음 위치가 나무나 맵 밖이면 그냥 pass 한다.
                ni, nj = ci + di[dir], cj + dj[dir]

                if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 'T':
                    ci, cj = ni, nj
            elif diractions[idx] =='R':
                dir = (dir + 1) % 4
            elif diractions[idx] == 'L':
                dir = (dir - 1) % 4

        # 모든 명령을 다 실행했을 때 위치가 Y면 1을 추가한다.
        if board[ci][cj] == 'Y':
            result.append(1)
        else:
            result.append(0)


    print(f"#{tc}", *result)
