import sys
sys.stdin = open('input.txt')

T = int(input())
T = 1

# 상 하 좌 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T+1):

    # 크기, 격리 시간, 군집 수
    N, M, K = map(int, input().split())

    micros = []

    for _ in range(K):
        I, J, count, direction = map(int, input().split())
        micros.append([I, J, count, direction])

    for _ in range(M):
        for m in micros:
            # 모든 격리시간마다 각각의 군집들은 정해진 방향을 향해 이동한다.
            # 또한 벽에 닿거나 같은 자리에 있을 경우 절반되고 방향이 반대가 되거나 병합된다.
            m[0] += di[m[3]]
            m[1] += dj[m[3]]

            # 만약 해당 군집이 벽에 닿을 경우
            if m[0] == 0 or m[0] == N - 1 or m[1] == 0 or m[1] == N - 1:
                m[2] //= 2

                # 방향이 반대가 된다.
                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                elif m[3] == 4: m[3] = 3

        # 그리고 만약 이동했을때 그 곳에 이미 군집이 있는경우 병합하는 로직을 수행한다.
        # 그러기 위해서는 먼저 micros 를 정렬한다.
        # 이러면 자연스럽게 군집을 병합하고 큰 군집의 방향을 따를 수 있다.
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











