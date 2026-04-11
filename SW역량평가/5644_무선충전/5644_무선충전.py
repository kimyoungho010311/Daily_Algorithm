import sys
sys.stdin = open('input.txt')
"""
10 * 10 지도가 주어진다.

일단 배터리의 충전 구역은 마름모 모양이다. 이건 맨헤튼거리 공식으로 구했던걸로 기억함
0, 1, 2, 3, 4는 가만히, 상, 우, 하, 좌로 있는다. 아래에 델타탐색방향 선언하기

일단 지도를 어떤식으로 구성해야할지 모르겠음
[[0], [0], [0]]
[[0], [0], [0]]
[[0], [0], [0]]
이런식으로 만들고 각 배터리의 충전 영역을 append해야하나? -> [10, 110] 이런식으로 겹친부분을 해결해야하나
위에 방법 말고는 다른 방법이 안떠오름

전체적인 지도를 구성한 다음에 사용자의 위치에 따라서 해당 값을 계속해서 더해나간다..
하지만 이런식으로 하면 같은 BC의 충전량을 나누지 못할것이고.. 또한 두 개의 BC영역에 겹칠 때 어느 하나를 고를지 모르겠다.

------------
잼미니한테 물어보니깐 지도그리지말고 리스트로 관리하면 편할거같다고 한다.
앞으로는 이런 문제가 나오면 무조건 지도만 떠오르는게 아니라 리스트도 한번 고민해봐야겠다.

BC정보를 리스트에 담아두고 [x, y, dist, power], 매 초마다 사용자의 위치 (ux, uy)와 모든 BC 사이의 거리를 계산한다.
abs(ux - bc_x) + abs(uy - bc_y) <= bc_dist

겹치는 구역의 문제는 브루트 포스로 해결한다.
매 초마다 사용자 A가 접속 가능한 BC리스트와 사용자 B가 접속 가능한 BC 리스트를 각각 구한다.
A가 선택 가능한 BC리스트와 B가 선택한 BC리스트를 이중 for문으로 돌리며 모든 조합의 합을 구하고 그 중 max 값을 찾는다.
"""

# 가만히, 상, 우, 하, 좌
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]

def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

T = int(input())
for tc in range(1, T + 1):
    # 이동 시간, BC의 수
    M, A = map(int, input().split())

    # 각 사용자의 이동 정보
    a_root = list(map(int, input().split()))
    b_root = list(map(int, input().split()))

    BC_list = []
    for _ in range(A):
        x, y, coverage, power = map(int, input().split())
        BC_list.append([x, y, coverage, power]) # [[4, 4, 1, 100], [7, 10, 3, 40], [6, 3, 2, 70]]

    # 각 사용자의 초기 위치
    a_pos = [1, 1]
    b_pos = [10, 10]

    total_charge = 0

    # 0초부터 M초까지 반복 (이동은 M번하지만, 위치는 M+1개임)
    for t in range(M + 1):

        # 현재 위치에서 충전 가능한 BC찾기
        A_can = []
        B_can = []

        for i in range(A):
            if get_dist(a_pos, BC_list[i][:2]) <= BC_list[i][2]:
                A_can.append(i)
            if get_dist(b_pos, BC_list[i][:2]) <= BC_list[i][2]:
                B_can.append(i)

        # 두 사람의 BC 조합 중 최대 충전량 찾기
        max_sum = 0

        # 접속 가능한 BC가 없을 경우에 대비해 더미 값 추가
        if not A_can: A_can.append(-1)
        if not B_can: B_can.append(-1)

        # 모든 조합을 다 시도해본다.
        for a_idx in A_can:
            for b_idx in B_can:
                current_sum = 0

                # 케이스 1: 둘 다 같은 BC를 선택한 경우
                if a_idx == b_idx:
                    if a_idx != -1:
                        # 반반 나눠도 합은 결국 해당 BC의 Power 하나 값
                        current_sum = BC_list[a_idx][3]

                # 케이스 2: 서로 다른 BC를 선택한 경우 (또는 한 명만 선택)
                else:
                    if a_idx != -1:
                        current_sum += BC_list[a_idx][3]
                    if b_idx != -1:
                        current_sum += BC_list[b_idx][3]

                max_sum = max(max_sum, current_sum)

        # 이본 초의 최대 충전량을 정답에 누적함
        total_charge += max_sum

        # 다음 위치로 이동 (마지막 t=M일떄는 이동하지 않음)
        if t < M:
            a_dir, b_dir = a_root[t], b_root[t]

            # 주어지는 방향은 맵 밖으로 나가지 않는다고 하니 무결성로직은 필요 없음
            a_pos[0] += dj[a_dir]
            a_pos[1] += di[a_dir]

            b_pos[0] += dj[b_dir]
            b_pos[1] += di[b_dir]

    print(f"#{tc} {total_charge}")