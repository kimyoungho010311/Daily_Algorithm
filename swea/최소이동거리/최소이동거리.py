import sys
sys.stdin = open('input.txt')
'''
단방향 그래프이다.
'''
import  heapq

def path():
    # 0번이 시작지점이다.
    pq = []
    heapq.heappush(pq, (0, 0))
    dist[0] = 0

    while pq:
        cost, curr_node = heapq.heappop(pq)

        if dist[curr_node] < cost:
            continue

        for next_node, weight in graph[curr_node]:
            new_cost = cost + weight

            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

T = int(input())

for tc in range(1, T + 1):

    N, E = map(int, input().split())

    INF = float('inf')
    dist = [INF] * (E)
    graph = [[] for _ in range(E)]

    for _ in range(E):
        s, e, w = map(int, input().split())

        graph[s].append((e, w))

    path()

    for elem in reversed(dist):
        if elem != INF:
            print(f"#{tc} {elem}")
            break