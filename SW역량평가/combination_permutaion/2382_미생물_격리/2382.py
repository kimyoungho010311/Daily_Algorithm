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

# 경계에 만나면 작동되는 함수
def reach_border():
    pass

# 한곳에 만나면 작동되는 함수
def merge():
    pass

T = int(input())
# T = 1 # For Test...

for tc in range(1, T+1):
    # 7, 2, 9
    N, M, K = map(int, input().split()) # 셀의 수, 격리 시간, 군집의 개수
    micros = [] # 군집들의 정보
    result = 0

    for _ in range(K):
        I, J, count, direction = map(int, input().split()) # 세로, 가로, 미생물 수, 이동방향
        # 상: 1, 하: 2, 좌: 3, 우: 4
        micros.append([I, J, count, direction])

    # matrix 를 사용해서 방향전환, 합치기 로직을 구현하기는 매우 까다롭다.
    # 방향 전환 로직이야 어떻게 구현한다고 해도
    # 병합되는 로직은 구현하기 힘들다.
    # 따라서 micros 자체에 인덱스값 미생물 값을 다뤄서
    # 최종적으로 합산하여 구하는 방식으로 한다.

    for _ in range(M):
        # 모든 군집 이동 및 가장자리 처리
        for m in micros:
            m[0] += di[m[3]]
            m[1] += dj[m[3]]

            if m[0] == 0 or m[0] == N-1 or m[1] == 0 or m[1] == N-1:
                m[2] //= 2 # 미생물 반토막
                # 방향 반전
                if m[3] == 1: m[3] = 2
                elif m[3] == 2: m[3] = 1
                elif m[3] == 3: m[3] = 4
                elif m[3] == 4: m[3] = 3
        # 이후 합치기 로직 작성!
        micros.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        new_micros = []
        if not micros: continue

        # 첫 번째 군집을 기준으로 시작
        current = micros[0]

        for i in range(1, len(micros)):
            # 다음 군집과 좌표가 같다면? 합치기!
            if micros[i][0] == current[0] and micros[i][1] == current[1]:
                current[2] += micros[i][2]
                # 이미 정렬을 했기 때문에, current의 방향이 무조건 가장 큰 군집의 방향임!
            else:
                # 좌표가 다르면 지금까지 합친 군집을 저장하고 새로 시작
                new_micros.append(current)
                current = micros[i]

        new_micros.append(current)  # 마지막 군집 추가
        micros = new_micros  # 업데이트

    for idx in range(len(micros)):
        result += micros[idx][2]

    # print(micros)
    print(f"#{tc} {result}")



