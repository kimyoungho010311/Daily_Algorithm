import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def DFS(start):
    dfs_ans.append(start)
    curr = start
    visited[curr] = True

    for next_node in adj_list[curr]:
        if not visited[next_node]:
            DFS(next_node)

def BFS(start):
    visited = [False] * (N + 1)
    q = deque()
    q.append(start)
    visited[start] = True
    bfs_ans.append(start)
    while q:
        curr = q.popleft()

        for next_node in adj_list[curr]:
            if not visited[next_node]:
                bfs_ans.append(next_node)
                visited[next_node] = True
                q.append(next_node)


# 정점의 수, 간선의 수, 시작 지점
N, M, V = map(int, input().split())
# 양방향 그래프이다.

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())

    adj_list[s].append(e)
    adj_list[e].append(s)

for i in range(len(adj_list)):
    adj_list[i].sort()

# DFS
dfs_ans = []
DFS(V)

bfs_ans = []
BFS(V)

print(*dfs_ans)
print(*bfs_ans)