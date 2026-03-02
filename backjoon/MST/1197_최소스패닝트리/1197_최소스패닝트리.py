# import sys
# sys.stdin = open('input.txt')
# """
#
# """
# import sys, heapq
# input = sys.stdin.readline
#
# def prim(start, V, adj):
#
#     visited = [False] * (V + 1)
#     pq = []
#
#     heapq.heappush(pq, (0, start))
#     total_weight = 0
#
#     while pq:
#         weight, node = heapq.heappop(pq)
#
#         if visited[node]:
#             continue
#         visited[node] = True
#         total_weight += weight
#
#         for next_node, next_weight in adj[node]:
#             if not visited[next_node]:
#                 heapq.heappush(pq, (next_weight, next_node))
#     return total_weight
#
#     # visited = [False] * (V+1)
#     # pq = []
#     #
#     # heapq.heappush(pq, (0, start))
#     # total_weight = 0
#     # while pq:
#     #     print(pq)
#     #
#     #     weight, node = heapq.heappop(pq)
#     #
#     #     if visited[node]:
#     #         continue
#     #     visited[node] = True
#     #     total_weight += weight
#     #
#     #     for next_node, next_weight in adj[node]:
#     #         if not visited[next_node]:
#     #             heapq.heappush(pq, (next_weight, next_node))
#     # return total_weight
#
# V, E = map(int, input().split())
# # Prim 알고리즘은 roots가 아니라 인접 리스트로 해야하는 듯
# adj = [[] for _ in range(V + 1)]
#
# for _ in range(E):
#     s, e, w = map(int, input().split())
#
#     adj[s].append((e, w))
#     adj[e].append((s, w))
#
# print(prim(1, V, adj))


def make_set(N):
    p = list(range(N+1))
    rank = [0] * (N+1)
    return p, rank

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    r_x = find_set(x)
    r_y = find_set(y)

    if p[r_x] != p[r_y]:
        if rank[r_x] > rank[r_y]:
            p[r_y] = r_x
        elif rank[r_x] < rank[r_y]:
            p[r_x] = r_y
        else:
            p[r_y] = r_x
            rank[r_x] += 1

def same(x, y):
    return find_set(x) == find_set(y)

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())

p, rank = make_set(V)
min_weight = 0
edges_cnt = 0
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A,B,C))

edges.sort(key=lambda x: x[2])

for s, e, w in edges:

    if not same(s, e):
        union(s, e)
        min_weight += w

print(min_weight)