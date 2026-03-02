import sys
sys.stdin = open('input.txt')
"""
"""
import sys, heapq
input = sys.stdin.readline

def prim(start, V, adj):
    visited = [False] * (V+1)
    pq = []

    heapq.heappush(pq, (0, start))  # (weight, node)
    total_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight

        for next_node, next_weight in adj[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_weight, next_node))  # (weight, node)

    return total_weight

# 컴퓨터(노드)의 수
V = int(input())
# 네트워크(간선)의 수
E = int(input())

adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))
    adj[e].append((s, w))

print(prim(1, V, adj))