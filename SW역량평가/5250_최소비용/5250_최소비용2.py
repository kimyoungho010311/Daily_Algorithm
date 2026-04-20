import sys
sys.stdin = open('input.txt')
"""
다익스트라이다.

출발지와 도착지는 항상 동일하다. 왼쪽끝, 오른쪽 아래
상하좌우로 인접 지역만 이동이 가능하다.

이동시에는 기본적으로 1의 연로가 들고 더 높은곳으로 이동할 경우 차이만큼 연료가 소모된다.

낮 -> 높은경우만 연료가 추가적을 소모된다. 높 -> 낮은 경우는 그냥 1만 소모된다.
"""
import heapq

def path():

    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    pq = []
    # 가중치, i, j
    heapq.heappush(pq, (0, 0, 0))
    # 시작지점의 가중치는 0
    distance[0][0] = 0

    while pq:
        cost, i, j = heapq.heappop(pq)

        # 기존에 저장된 값이 더 작으면 무시
        # if distance[i][j] < cost:
        #     continue

        # 일단 다음 좌표를 구한 다음에
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            # 해당 좌표가 방문한적 없고(INF가 아니고) 지도안에 있다면 다익스트라 탐색을 시작한다.
            if 0 <= ni < N and 0 <= nj < N:
                diff = 0
                # 만약 해당 지점의 값이 높으면 그냥 넘어가고
                if board[i][j] < board[ni][nj]:
                    diff = board[ni][nj] - board[i][j]
                # 아니라면 아래 로직을 실행한다.
                curr_cost = cost + diff + 1

                if distance[ni][nj] > curr_cost:
                    distance[ni][nj] = curr_cost
                    heapq.heappush(pq, (curr_cost, ni, nj))

T = int(input())
for tc in range(1, T+1):

    # 배열 크기
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]

    path()

    print(f"#{tc} {distance[N-1][N-1]}")