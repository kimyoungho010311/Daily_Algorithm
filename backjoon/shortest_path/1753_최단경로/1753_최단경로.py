import sys
sys.stdin = open('input.txt')
"""

"""
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start, V, adj):
    dist = [float('inf')] * (V+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d: continue

        for v, weight in adj[u]:
            cost = d + weight # 누적 거리 계산
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))
    return dist


# 정점의 개수, 간선의 수
V, E = map(int, input().split())
start = int(input())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())

    adj[s].append((e, w))

result = dijkstra(start, V, adj)

for idx in range(1, len(result)):
    if result[idx] == float('inf'):
        print("INF")
    else:
        print(result[idx])