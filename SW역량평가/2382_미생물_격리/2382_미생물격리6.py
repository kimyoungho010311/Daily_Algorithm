import sys
sys.stdin = open('input.txt')
"""
각 군집들은 리스트로 다룬다.

"""

# 상 하 좌 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    # 셀의 개수, 격리 시간, 미생물의 군집의 개수
    N, M, K = map(int, input().split())
    micros = []

    for _ in range(K):
        i, j, count, dir = map(int, input().split())
        micros.append([i, j, count, dir])

    for _ in range(M):

        for m in micros:
            m[0] += di[m[3]]
            m[1] += dj[m[3]]

            # 만약 군집이 가장자리에 위치한다면
            if m[0] == 0 or m[0] == N-1 or m[1] == 0 or m[1] == N-1:
                # 군집의 수를 반띵해주고 방향을 바꿔준다.
                # (상: 1, 하: 2, 좌: 3, 우: 4)
                m[2] //= 2

                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                elif m[3] == 4: m[3] = 3

        # 모든 군집들의 위치 조정이 끝나고 같은 위치에 있는 군집들에 대한 계산을 한다.
        # 큰 군집에 흡수되면서 방향이 유지된다.
        # 즉 i, j, count 순서대로 정렬해 준다음에 new_micor에 하나씩 더한 값을 append해주고
        # 마지막에 micros에 저장해준다.

        micros.sort(key= lambda x: (x[0], x[1], x[2]), reverse=True)

        new_micros = []
        curr_micros = micros[0]

        for i in range(1, len(micros)):
            # 만약 같은 위치라면
            if curr_micros[0] == micros[i][0] and curr_micros[1] == micros[i][1]:
                # 현재 군집의 다 넣어준다.
                curr_micros[2] += micros[i][2]
            else: # 위치가 다른 군집이 선택된다면 지금까지 모았던 군집을 new_micros에 넣어준다.
                new_micros.append(curr_micros)
                curr_micros = micros[i]
        new_micros.append(curr_micros)
        micros = new_micros

    ans = 0
    for idx in range(len(micros)):
        ans += micros[idx][2]

    print(f"#{tc} {ans}")




