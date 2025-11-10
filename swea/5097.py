t = int(input())

for t in range(t):
  N, M = map(int,input().split())

  arr = input().split()

  for i in range(M):
    tmp = arr[0]
    del arr[0]
    arr.append(tmp)

  print(f"#{t+1} {arr[0]}")