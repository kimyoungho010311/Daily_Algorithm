import sys
sys.stdin = open('input.txt')

'''
N * N 구역에 K 개의 미생물 '군집'이 있다.
이 미생물들이 M시간후에 총 얼마나 남아있는지 출력한다.

RULES
1. 미생물이 가장자리에 도착하면 원래 미생물 수 / 2로 나눈 후 소숫점 이하를 버림한 값이다.
   만약 0이되면 군집이 사라지게 된다. <- 이거 히든 테케일듯
2. 군집이 한곳에 모이면 미생물의 수가 합쳐지며, 가장 큰 군집의 진행 방향을 따른다.

[1, 1, 1, 1, 1, 1, 1]
[1, 7, 0, 0, 0, 8, 1]
[1, 7, 0, 0, 0, 0, 1]
[1, 0, 8, 0, 3, 100, 1]
[1, 0, 0, 14, 0, 0, 1]
[1, 5, 0, 0, 0, 1, 1]
[1, 1, 1, 1, 1, 1, 1]

'''

# 상 하 좌 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) # 셀의 수, 격리 시간, 군집의 개수
    micros = []
    result = 0
    for _ in range(K):
        I, J, count, direction = map(int, input().split())
        # 상: 1, 하: 2, 좌: 3, 우: 4
        micros.append([I, J, count, direction])

    for _ in range(M):

        # 모든 군집 이동 및 가장자리 처리
        for m in micros:
            # micros에서 주어진 방향대로 벽을 만날 때 까지 전진한다.
            m[0] += di[m[3]]
            m[1] += dj[m[3]]

            # 그러다 만약 벽을 만났을 경우 반띵당하고 방향을 반대로 전환한다.
            if m[0] == 0 or m[0] == N - 1 or m[1] == 0 or m[1] == N - 1:
                m[2] //= 2 # 만약 미생물이 벽에 닿으면 반토막낸다.

                # 방향 반전
                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                elif m[3] == 4: m[3] = 3

        # 여기 아래는 전부 같은 위치에 있을시에 합치는 로직이다.
        # 아래처럼 정렬을 하게 된다면 자연스럽게 같은 위치에 (x[0], x[1]) 있는 군집끼리 모이게 될것이고
        # reverse를 하면 가장 큰 군집이 앞에 나오게 될 것이다.
        micros.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        new_micros = []
        # 아래는 약간의 안전장치 느낌이다.
        # 만약 micros 리스트가 비어있는데 64번째 코드를 실행하면 에러가 남으로
        # 리스트가 비어있으면 넘어가 오류를 피한다.
        if not micros: continue

        # 첫 번째 군집을 기준으로 시작
        current = micros[0] # 같은 위치에서 가장 큰 군집이 선택된다.

        for i in range(1, len(micros)):
            # 다음 군집과 좌표가 같다면 합치기
            if micros[i][0] == current[0] and micros[i][1] == current[1]:
                current[2] += micros[i][2]
                # 이미 정렬을 했기 때문에, current의 방향이 무조건 가장 큰 군집의 방향임
            else:
                # 좌표가 다르면 지금까지 합친 군집을 저장하고 새로 시작
                new_micros.append(current)
                current = micros[i]

        new_micros.append(current)
        micros = new_micros

    for idx in range(len(micros)):
        result += micros[idx][2]

    print(f"#{tc} {result}")
