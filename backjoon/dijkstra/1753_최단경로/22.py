import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, curr_node = heapq.heappop(pq)

        if dist > distance[curr_node]:
            continue

        for next_node, cost in graph[curr_node]:
            new_cost = dist + cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))


# 정점의 수, 간선의 수
V, E = map(int, input().split())

# 시작 정점의 번호
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('inf')
distance = [INF] * (V+1)

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])