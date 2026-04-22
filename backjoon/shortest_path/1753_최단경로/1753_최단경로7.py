import sys
sys.stdin = open('input.txt')
import heapq

def path(start):
    pq = []
    heapq.heappush(pq, (0, K))
    dist[K] = 0

    while pq:
        cost, curr_node = heapq.heappop(pq)

        if dist[curr_node] < cost:
            continue

        for next_node, weight in graph[curr_node]:
            new_cost = cost + weight

            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

V, E = map(int, input().split())
K = int(input())

INF = float('inf')
dist = [INF] * (V + 1)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

path(K)

for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
