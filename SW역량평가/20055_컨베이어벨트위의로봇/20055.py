import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, input().split())
Ai = list(map(int, input().split()))
belt_length = N
phase = 0

belt_up = deque(Ai[:N])
belt_down = deque(Ai[N:])

box_position = deque([False] * N)

while True:
    phase += 1

    belt_up.appendleft(belt_down.pop()) # 아랫벨트 끝이 윗벨트 처음으로
    belt_down.appendleft(belt_up.pop())     # 윗벨트 끝이 아랫벨트 처음으로
    box_position.rotate(1)              # 로봇도 같이 한 칸 이동

    # 회전 직후 내리는 위치에 로봇이 있다면 즉시 하차
    box_position[N-1] = False

    # 가장 먼저 올라간 상자부터 한 칸 이동
    for i in range(N-2, -1, -1):
        # 내가 로봇이 있고, 다음 칸에 로봇이 없고, 다음 칸의 내구도가 1 이상이면
        if box_position[i] == True and box_position[i+1] == False and belt_up[i+1] >= 1:
            box_position[i] = False
            box_position[i+1] = True
            belt_up[i+1] -= 1

    # 이동 후에도 내리는 위치에 박스가 있다면 즉시 하차
    box_position[N-1] = False

    # 올리는 위치 내구도가 0이 아니면 상자 올리기
    if belt_up[0] > 0:
        box_position[0] = True
        belt_up[0] -= 1

    zero_count = belt_up.count(0) + belt_down.count(0)
    if zero_count >= K:
        break
print(phase)