import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dijsktra(start):

    pq = []
    heapq.heappush(pq,(0, start))
    distance[start] = 0

    while pq:
        dist, curr_node = heapq.heappop(pq)

        if distance[curr_node] < dist:
            continue

        for next_node, weight in graph[curr_node]:
            new_cost = dist + weight

            if distance[next_node] > new_cost:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

# 정점 수, 간선 수
V, E = map(int, input().split())
# 시작 지점
K = int(input())

graph = [[] for _ in range(V + 1)]
INF = float('inf')
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijsktra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])