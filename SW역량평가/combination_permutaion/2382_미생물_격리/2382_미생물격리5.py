import sys
sys.stdin = open('input.txt')
"""
N * N 개의 크기의 셀로 이루어져 있다.
가장자리에는 특수한 약품이 발라져 있다.

미생물 군집의 위치, 미생물 수, 이동 방향이 주어지며 약품처리된 곳에는 없다.
이동방향은 상 하 좌 우 네 방향 중 하나이다.

한시간마다 이동방향에 있는 셸로 이동한다.

만약 약품에 닿으면 반띵 당하고 반대방향으로 움직인다.
(홀수이면 int() 처리한다.)
만약 군집이 0이된다면 그냥 사라진다.

한 셀에 여러 군집이 겹치면, 큰 크기의 이동방향으로 이동하며 두 군집이 합쳐진다.
합쳐지는 미생물의 수가 같은 경우는 없다.

M 시간 이후 남아있는 미생물의 수의 총합은?
================================================================================
이게 왜 순열조합이지..?
단순히 최소 최대의 미생물 수를 구하는게 아니라 주어진 명령에 따라 실행 했을 경우 남아 있는 미생물 수를 출력하는거 같다.

내 기억상으로는 각 군집들을 리스트로 다루고 델타 탐색을 통해 약품에 닿았을 경우, 군집이 합쳐지는 경우
딱 두가지의 로직만 구현하면 되는걸로 기억한다.

특히 합쳐질 때는 리스트(군집)의 미생물 수를 정렬해서 간단히 더하는 것으로 마무리 했던걸로 기억한다.
레츠고
"""

T = int(input())

# 상: 1, 하:2, 좌:3, 우:3
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T + 1):

    # 군집의 정보는 세로(i), 가로(j)로 주어진다.

    # 지도 크기, 격리 시간, 군집 개수
    N, M, K = map(int, input().split())

    # 군집 리스트
    micros = []

    for _ in range(K):
        # 세로, 가로, 미생물 수, 이동방향
        i, j, micro_cnt, dir = map(int, input().split())
        micros.append([i, j, micro_cnt, dir])

    # 시간마다 각 군집의 이동 방향에 따라 로직을 구현한다.
    for _ in range(M):

        for m in micros:
            # 군집의 ni, nj를 구한다.
            m[0] += di[m[3]]
            m[1] += dj[m[3]]

            if m[0] == 0 or m[0] == N-1 or m[1] == 0 or m[1] == N-1:
                # 만약 ni, nj가 약품에 닿는다면
                # int(micros[2] / 2) 처리 한 다음 현재 dir의 반대 방향을 직접 매핑해준다.
                m[2] //= 2

                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                else: m[3] = 3
            # 만약 ni, nj에 다른 군집이 있다면
            # 그 위치에 다른 군집이 있다는걸 어케 확인하지..?

        # 군집을 합치기 쉽게 정렬해준다.
        micros.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        new_micros = []
        current = micros[0]


        for i in range(1, len(micros)):
            if micros[i][0] == current[0] and micros[i][1] == current[1]:
                current[2] += micros[i][2]
            else:
                new_micros.append(current)
                current = micros[i]
        new_micros.append(current)
        micros = new_micros

    result = 0
    for idx in range(len(micros)):
        result += micros[idx][2]

    print(f"#{tc} {result}")























    pass