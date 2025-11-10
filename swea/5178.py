T = int(input())

for tc in range(1, T+1):
  N, M, L = map(int,input().split())

  tree = [0] * (N+1)

  for i in range(M):
    a, b = map(int,input().split())
    tree[a] = b
  
  for i in range(N, 0, -1):
    if 2*i <= N:
      if 2*i+1 <= N:
        tree[i] = tree[2*i] + tree[2*i+1]
      else:
        tree[i] = tree[2*i]
  print(f"#{tc} {tree[L]}")