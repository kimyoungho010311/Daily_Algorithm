import sys
sys.stdin = open('input.txt')

T = int(input())

# 상 하 좌 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T+1):
    # 지도 크기, 격리 시간, 군집 수
    N, M, K = map(int, input().split())

    micros = []

    for _ in range(K):
        I, J, count, direction = map(int, input().split())
        micros.append([I, J, count, direction]) # 1 1 7 1

    # 격리 시간 만큼 반복한다.
    for _ in range(M):

        for m in micros:
            m[0] += di[m[3]]
            m[1] += dj[m[3]]

            if m[0] == 0 or m[0] == N - 1 or m[1] == 0 or m[1] == N - 1:
                m[2] //= 2

                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                elif m[3] == 4: m[3] = 3

        micros.sort(key= lambda x:(x[0], x[1], x[2]), reverse=True)

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