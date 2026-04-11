import sys
sys.stdin = open('input.txt')
"""

"""
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    # 시작지점은 거리를 0으로 잡는다.
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
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

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])