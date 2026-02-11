T = int(input())

for tc in range(T):
  N = int(input())
  sum = 0
  for i in range(1, N):
    if i % 2 != 0:
      sum -= i
    else:
      sum += i
  print(f"#{tc+1} {sum}")