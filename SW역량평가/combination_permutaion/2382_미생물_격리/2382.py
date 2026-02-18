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
T = 1 # For Test...

for tc in range(1, T+1):
    # 7, 2, 9
    N, M, K = map(int, input().split()) # 셀의 수, 격리 시간, 군집의 개수
    micros = [] # 군집들의 정보

    for _ in range(K):
        I, J, count, direction = map(int, input().split()) # 세로, 가로, 미생물 수, 이동방향
        # 상: 1, 하: 2, 좌: 3, 우: 4
        micros.append([I, J, count, direction])

    # 가장자리를 약품질해서 미생물을 가둔다.
    mat = [[1] * N for _ in range(N)] # N: 7
    for i in range(N):
        for j in range(N):
            if 0 < i < N-1 and 0 < j < N-1:
                mat[i][j] = 0

    # 여기 아래 반복문도 딱히 필요 없을 듯?
    for idx in range(K):
        mat[micros[idx][0]][micros[idx][1]] = micros[idx][2]

    mat_copy = [row[:] for row in mat]

    # 이렇게 한번에 모든 군집에 적용할려고 하지말고
    # 하나의 군집을 먼저 정한다음에 해당 군집만 움직이도록 해보자

    # 먼저 진행방향으로 움직이는 로직 설계해 보자

    for _ in range(M): # M 시간동안 M번 움직여야 함
        for idx in range(K): # 각 군집을 반복적으로 해야하기 때문에 micros 배열을 순회한다.
            direction = micros[idx][3] # 각 군집의 이동 방향을 받은 다음에
            ni, nj = micros[idx][0] + di[direction], micros[idx][1] + dj[direction]

            if 0 < ni < N-1 and 0 < nj < N-1 and mat_copy[ni][nj] != 1:
                mat_copy[micros[idx][0]][micros[idx][1]] = 0 # 지금 있었던 위치의 값을 초기화하고
                mat_copy[ni][nj] = micros[idx][2] # 다음 위치에 미생물 값을 입력한다.
            else: # 만약 약품에 닿는다면
                # print(micros[idx][2])
                micros[idx][2] = int(micros[idx][2] / 2) # 2로 나눈 후 소숫점 이하를 버림 한 값이 되고
                print(micros[idx][2])
                if direction == 1: direction = 2
                elif direction == 2: direction = 1
                elif direction == 3: direction = 4
                elif direction == 4: direction = 3

                nni, nnj = micros[idx][0] + di[direction], micros[idx][1] + dj[direction]
                if 0 < nni < N-1 and 0 < nnj < N-1 and mat_copy[nni][nnj] != 1:
                    mat_copy[nni][nnj] = micros[idx][2]

    # for row in mat_copy:
    #     print(row)









