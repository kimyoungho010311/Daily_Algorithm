import sys
sys.stdin = open('input.txt')
"""
"""

# 상 하 좌 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())
T = 1

for tc in range(1, T+1):
    # 지도 크기, 격리 시간, 군집 수
    N, M, K = map(int, input().split())
    result = 0
    micros = []
    for _ in range(K):
        I, J, count, direction = map(int, input().split())
        micros.append([I, J, count, direction])

    
    # 이제 M번만큼 시간이 지날 떄 군집들의 상태를 계산한다.
    for _ in range(M):
        for m in micros:
            # next_i
            m[0] += di[m[3]]
            # next_j
            m[1] += dj[m[3]]

            if m[0] == 0 or m[0] == N - 1 or m[1] == 0 or m[1] == N - 1:
                m[2] //= 2

                # 여기서 방향을 반대로 반전시킨다.
                # (상: 1, 하: 2, 좌: 3, 우: 4)
                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                elif m[3] == 4: m[3] = 3

            # 소멸된 군집은 제거 한다. (선택 사항)

        micros = [m for m in micros if m[2] > 0]
        if not micros: break # 모든 미생물이 사라지면 종료

        # 이렇게 하면 동일한 위치에 가장 큰 군집이 맨 앞에 나오게 된다.
        micros.sort(key= lambda x: (x[0], x[1], x[2]), reverse=True)

        new_micros = []
        current = micros[0] # [5, 1, 5, 4]

        for i in range(1, len(micros)):
            # 만약 동일한 위치에 있을 시엔
            if micros[i][0] == current[0] and micros[i][1] == current[1]:
                current[2] += micros[i][2]
            else:
                new_micros.append(current)
                current = micros[i]
        new_micros.append(current)
        micros = new_micros

    for idx in range(len(micros)):
        result += micros[idx][2]

    print(f"#{tc} {result}")