import sys
sys.stdin = open('input.txt')
"""
길이가 N인 컨베이어
2N인 컨베이어 벨트

Ai = 내구도 리스트

1번칸 -> 올리는 위치
N번칸 -> 내리는 위치

로봇은 올리는 위치에만 올릴 수있다. 로봇이 내리는 위치에 도달하면 즉시 내린다.
로봇은 컨베이어 위에서 움직일 수 있다. 로봇이 위치한 칸은 내구도 1 감소한다.

1. 벨트가 각 칸 위에 있는 로봇고 ㅏ함께 한 칸 회전한다.
2. 가장 먼저 올라간 상자부터 이동 가능하면 앞으로 옮긴다.
    2-2. 해당칸에 아무것도 업성야하며, 내구도가 1이상이어야한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 상자를 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료. 아니면 1번으로 돌아간다.
"""
# 리스트를 총 두개 생성한다. belt_up, belt_down 이런 식으로... 그래야 벨트 내구도를 옮기는데 무리 없을 듯
# 리스트는 총 2천개까지 가능 복잡도는 O(2000)이면 ... 빠를듯?
# 상자는 어떤 식으로 옮겨야 하는가?
# boxs = [] 해가지고 boolean 값을 사용해 박스의 위치는 idx 값으로 다루면 좋을듯
# 박스의 위치도... 하나씩 옮겨야해서 O(1000)까지 나오면 충분
from collections import deque


N, K = map(int, input().split())
Ai = list(map(int, input().split()))
belt_length = len(Ai) // 2
phase = 0 # 일단 0 단계가 끝나고 작업이 모두 끝나는 순간에 1 더해야 정답이 맞을듯

box_position, belt_up, belt_down = [False] * belt_length, deque([]), deque([])

for i in range(len(Ai)):
    if i < belt_length:
        belt_up.append(Ai[i]) # [1, 2, 1]
    else:
        belt_down.append(Ai[i]) # [2, 1, 2]
belt_down.reverse()

test_list = [1, 2, 3, 4 , 5]

for i in range(len(test_list)-2, -2, -1):
    print(test_list[i+1])


#
while True:
    """
    1. 벨트가 각 칸 위에 있는 로봇고 ㅏ함께 한 칸 회전한다.
    2. 가장 먼저 올라간 상자부터 이동 가능하면 앞으로 옮긴다.
        2-2. 해당칸에 아무것도 업성야하며, 내구도가 1이상이어야한다.
    3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 상자를 올린다.
    4. 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료. 아니면 1번으로 돌아간다.
    """
    # 먼저 박스를 올리고 (시작과 마지막은 항상 비워야하기 떄문에 검사 로직을 맨 앞에 둔다)
    # 박스를 최대한 우측으로 이동시킨다음에
    # 컨베이어벨트를 움직이고
    # 내구도 검사를 한다
    # 4번 로직을 어디다 해야할까..?

    if box_position[0] == False: # 만약 박스를 올릴 수 있으면
        box_position[0] = True # 박스를 올려놓는다.
        belt_up[0] -= 1 # 그리고 해당 컨베이어의 내구도를 깎는다.

    if box_position[-1] == True: # 박스가 내리는 곳에 도착하면
        box_position[-1] = False # 내린다.

    for i in range(belt_length-2, -2, -1):
        if box_position[i+1] == False and belt_up[i+1] >= 1: # 만약 앞에 칸에 박스가 없고 내구도가 남아 있다면
            box_position[i] = False # 박스를 우측으로 한칸 옮긴다.
            box_position[i+1] = True

    # 이제 여기서부터 컨베이어 벨트를 우측으로 옮기는 작업을 한다.
    # 또한 상자도 같이 옮겨야 한다.
    # 이렇게 상자를 움직이는 로직을 두 번 하는게 맞나..?
    for i in range(belt_length-2, -2, -1):
        if box_position[i+1] == False and belt_up[i+1] >= 1: # 만약 앞에 칸에 박스가 없고 내구도가 남아 있다면
            box_position[i] = False # 박스를 우측으로 한칸 옮긴다.
            box_position[i+1] = True
    belt_down.append(belt_up.pop())
    belt_up.appendleft(belt_down.popleft())

    phase += 1

    if K == belt_up.count(0) + belt_down.count(0):
        break
print(phase)