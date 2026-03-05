import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
N개의 도시가 있다.
M개의 버스가 있다.

A ~ B 도시로 가는데 드는 버스 비용을 최소화 시키려고 한다.
최소 비용을 출력해라.

출발에서 도착까지 갈 수 있는 경우만 주어진다.
"""

def dijkstra(start, N, adj_list):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq,(0, start)) # 반드시 가중치를 맨 앞에써야 정렬된다.

    while pq: # [inf, 0, 2, 3, 1, 4]
        d, u = heapq.heappop(pq) # 가중치, 현재 위치(노드)

        if dist[u] < d: # 이게 왜 방문처리가 되는거지?
            continue

        for v, w in adj_list[u]:
            cost = d + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))
    result = dist[end]
    print(dist)
    print(result)

# 도시
N = int(input())
# Bus
M = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj_list[s].append((e, w))

start, end = map(int, input().split())

dijkstra(start, N, adj_list)