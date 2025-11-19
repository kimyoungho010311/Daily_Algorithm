T = int(input())

for tc in range(T):
  test_case = int(input())
  N = list(map(int, input().split()))

  avg = int(sum(N)/len(N))

  cnt = 0
  for i in range(test_case):
    if N[i] <= avg:
      cnt += 1
  
  print(f"#{tc+1} {cnt}")