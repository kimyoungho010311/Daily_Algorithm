import sys
#bfs 
# queue
# 큐가 빌떄까지 무한 반복함
# 방문 리스트에 추가하기
# cur
# 그래프에 넣고
# 큐에 시작 지점 입력하고 알고리즘 시작
# 마지막에 리스트의 길이를 반환하면 될듯
# def bfs(V):
#   global q, visited, corrupted_pc
#   while q:
#     cur = q.pop(0)
#     corrupted_pc.append(cur)
#     for next in range(1, N + 1):
#       if not visited[next] and grahp[cur][next]:
#         visited[next] = True
#         q.append(next)

def dfs(idx):
  global visited
  visited[idx] = True
  corrupted_pc.append(idx)
  for next in range(1, N + 1):
    if not visited[next] and grahp[idx][next]:
      dfs(next)

# input
input = sys.stdin.readline

N = int(input()) # 컴퓨터 수
M = int(input()) # 간선의 수
corrupted_pc = []

# graph
grahp = [[False] * (N + 1) for i in range(N + 1)]
#visited
visited = [False] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  grahp[a][b] = True
  grahp[b][a] = True

# 큐 생성
dfs(1)
# 시작지점을 뺴기 위해 -1 을 한다.
print(len(corrupted_pc)-1)