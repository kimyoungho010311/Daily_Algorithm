import sys
def dfs(idx):
  global visited, graph
  visited[idx] = True
  print(idx, end= ' ')
  for next in range(1, N + 1):
    if not visited[next] and graph[idx][next]:
      dfs(next)

def bfs():
  global q, visited, graph
  while q:
    cur = q.pop(0)
    print(cur, end= ' ')
    for next in range(1, N + 1):
      if not visited[next] and graph[cur][next]:
        q.append(next)
        visited[next] = True


# 입력 받기
input = sys.stdin.readline

N, M, V = map(int,input().split())
# 그래프, 방문 리스트 만들기
graph = [[False] * ( N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
# 그래프 채우기

for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

# dfs
dfs(V)
print()

# bfs
q = [V]
visited = [False] * (N + 1)
visited[V] = True
bfs()