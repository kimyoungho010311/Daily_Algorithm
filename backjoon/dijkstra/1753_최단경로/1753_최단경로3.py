import sys
sys.stdin = open('input.txt')

import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

# 정점 수, 간선 수
V, E = map(int ,input().split())

# 시작지점
K = int(input())

graph = [[] for _ in range(V + 1)]

INF = float('inf')
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])