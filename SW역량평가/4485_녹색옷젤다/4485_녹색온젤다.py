import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
링크가 정신병 걸리기 직전임
N*N에서 [0][0] -> [N-1][N-1]로 갈거다.

이동할때 해당 지점에 적힌 수만큼 돈을 뜯겨야 한다.
최소한으로 뜯기는 비용은?

BFS + 다익스트라?
"""
def find_root(start, board):
    # 2차원 dist를 만든다.
    # 그 다음 BFS로 델타 탐색을 하면서
    # 해당 위치의 값을 계속해서 갱신하며
    # 각 위치로 가는데 최솟값을 담고있는 2차원 dist를 완성한다.
    # 출력하면 그만..

    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = board[0][0] # 시작하자마자 돈 뜯기고 시작하니깐 값 이렇게 초기화

    pq = []
    heapq.heappush(pq, (board[0][0], start))

    while pq:
        curr_acc, curr = heapq.heappop(pq) # 0 (0, 0)
        curr_i, curr_j = curr

        # 만약 지금까지 구한 최소거리 < 현재 탐색중인 누적값
        # 이면 연산 가치가 없으므로 그냥 넘어간다.
        if dist[curr_i][curr_j] < curr_acc:
            continue

        for k in range(4):
            ni, nj = curr_i + di[k], curr_j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                # 지금까지 누적값이랑 다음 위치의 합
                cost = curr_acc + board[ni][nj]
                
                # 지금 새로 구한 값이 내가 기존에 구했던 가중치보다 적으면
                # 해당 위치의 가중치 갱신
                if cost < dist[ni][nj]:
                    dist[ni][nj] = cost
                    heapq.heappush(pq, (cost,( ni, nj)))
    return dist[N-1][N-1]


cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    start = (0, 0)
    result = find_root(start, board)

    print(f"Problem {cnt}: {result}")
    cnt += 1