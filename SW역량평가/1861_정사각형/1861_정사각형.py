import sys
sys.stdin = open('input.txt')
"""
N * N형태의 방
1 ~ N^2수가 있으며 숫자는 모두 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동이 가능하다.
물론 이동하려는 방이 존재해야하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커 야한다.
처음에 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성
"""
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    can_go = [0] * (N*N + 1) # 다음 숫자로 갈 수 있는지 체크하는 배열
    room = []

    for _ in range(N):
        tmp = list(map(int, input().split()))
        room.append(tmp)

    for i in range(N):
        for j in range(N):
            curr = room[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if curr + 1 == room[ni][nj]:
                        can_go[curr] = 1

    max_len, curr_len, final_start = 0, 0, 0

    for i in range(N*N, -1, -1):
        if i > 0 and can_go[i] == 1:
            curr_len += 1
        else:
            # 1이 끊기는 순간(또는 시작점), 지금까지의 길이 체크
            # curr_len + 1을 하는 이유는 '이동 횟수'가 아니라 '방의 개수'이기 때문
            if curr_len >= max_len:
                max_len = curr_len
                final_start = i + 1# 연속이 시작된 숫자
            curr_len = 0

    print(f"#{tc} {final_start} {max_len + 1}")
