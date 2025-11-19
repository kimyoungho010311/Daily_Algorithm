import sys

def bfs(si, sj, ei, ej):
  q = [(si, sj)]
  v = [[0] * M for _ in range(N)]

  v[si][sj] = 1

  while q:
    ci, cj = q.pop(0)
    # 정답 처리가 필요한 경우 여기에..
    if (ci, cj) == (ei, ej):
      return v[ei][ej]

    # 4방향, 범위 내, 조건에 맞으면 큐에 삽입
    # : arr == 1, v == 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      ni, nj = ci+di, cj+dj
      if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]==1 and v[ni][nj]==0:
        q.append((ni, nj))
        v[ni][nj] = v[ci][cj]+1





input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

ans = bfs(0, 0, N-1, M-1)
print(ans)