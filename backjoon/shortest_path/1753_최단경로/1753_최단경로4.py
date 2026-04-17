import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:

        cost, curr_node = heapq.heappop(pq)

        if distance[curr_node] < cost:
            continue

        for next_node, weight in adj_list[curr_node]:
            new_cost = cost + weight

            if distance[next_node] > new_cost:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V+1)]
INF = float('inf')
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

dijkstra(K)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])