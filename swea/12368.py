T = int(input())

for tc in range(T):
  A, B = map(int,input().split())
  start = 0

  start += A
  result = start + B

  if result >= 24:
    result -= 24

  print(f"#{tc+1} {result}")

