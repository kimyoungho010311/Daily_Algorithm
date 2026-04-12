import sys
sys.stdin = open('input.txt')
"""
출발 ~ 도착지까지 가야하는데 높이에 따라 연료 소비량이 달라진다.
최소한의 연료를 구해라
인접하는데 가는건 1이 들고 높이에 따라 그 만큼 더 들어간다.
츌발은 (0,0) 도착은 (N-1, N-1)이다.
같은 높이라면 추가적인 연료 소모는 없다.

이 문제가 과연 다익스트라인가..? 일단 맞긴 한거같다 그래프에 가중치가 있고 음수 가중치가 없으니깐.
하지만 가중치가 주어진게 아니고, 지도로 주어지니깐 뭔가 BFS가 더 편리할거같긴하다. -> 아니라고 한다. BFS는 반드시 모든 가중치가 동일해야한다.

다익스트라 알고리즘을 적용한다면..
각 노드까지 가는데 소모되는 최소 비용을 가진 2차원 배열인 dist를 만들어야한다.
처음 dist를 선언할 떄는 INF로 리스트를 채우고... 시작점은 0으로 만든다 

그 다음 시작노드에서부터 델타탐색으로 각 노드로 이동한다.
각 노드에 이동하면 기본적으로 1이 들고 더 높은곳으로 가는거라면 그 높이만큼 연료 소비량이 늘어난다. (높 -> 낮 으로 가는건 어떻게 되는지 설명이 안되어있음)

만약 curr < next 라면 cost += next - curr 하면 될듯
이렇게 주어진 cost로 dist를 하나씩 채워나간뒤

마지막으로 dist[N-1][N-1]을 출력하면 마무리
"""
import heapq

def dijkstra(start):

    pq = []

    # 비용, i, j
    heapq.heappush(pq, (0, 0, 0))
    dist[0][0] = 0

    while pq:
        curr_w, i, j = heapq.heappop(pq)

        # 기존에 저장된 값이 더 작으면 무시
        if dist[i][j] < curr_w:
            continue

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                # 기본 비용 1 + 높이 차이
                diff = 0
                if board[ni][nj] > board[i][j]:
                    diff = board[ni][nj] - board[i][j]

                cost = curr_w + diff + 1

                # 갱신 로직
                if cost < dist[ni][nj]:
                    dist[ni][nj] = cost
                    heapq.heappush(pq, (cost, ni, nj))


# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    # 가로, 세로칸
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]

    start = [0, 0]
    end = [N-1, N-1]

    dijkstra(start)

    print(f"#{tc} {dist[N-1][N-1]}")