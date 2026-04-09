# 정점의 개수, 간선의 수, 시작지점
import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start):
    visited = [False] * (N+1)
    q = deque([start])
    visited[start] = True

    res = []
    res.append(start)
    while q:
        curr_node = q.popleft()

        for next_node in adj_matrix[curr_node]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True

                res.append(next_node)
    return res



def DFS(start, res):
    res.append(start)
    visited[start] = True

    for curr_node in adj_matrix[start]:
        if not visited[curr_node]:
            DFS(curr_node, res)

    return res
N, M, V = map(int, input().split())
adj_matrix = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_matrix[s].append(e)
    adj_matrix[e].append(s)

for mat in adj_matrix:
    mat.sort()

ans_bfs = BFS(V)

visited = [False] * (N + 1)
res = []
ans_dfs = DFS(V, res)
print(*ans_dfs)
print(*ans_bfs)
