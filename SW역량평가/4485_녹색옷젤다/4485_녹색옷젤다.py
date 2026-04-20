import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
왼쪽 끝에서 오른쪽 끝으로 이동해야한다.
각 칸 마다 도두룩 루피가 있는데 이 칸을 지나면 해당 칸만큼의 소지금을 잃게 된다.
이 금액을 최소로하여 한다

다익스트라임 가중치 = 잃는 돈 이라고 했을때 가장 작에 해야하는거 찾으면 된다.
"""

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def path():
    pq = []
    # cost, i, j
    heapq.heappush(pq, (board[0][0], 0, 0))
    dist[0][0] = board[0][0]

    while pq:
        cost, i, j = heapq.heappop(pq)

        if dist[i][j] < cost:
            continue

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                new_cost = cost + board[ni][nj]

                if dist[ni][nj] > new_cost:
                    dist[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
tc = 1
while True:
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    path()

    print(f"Problem {tc}: {dist[N-1][N-1]}")
    tc += 1