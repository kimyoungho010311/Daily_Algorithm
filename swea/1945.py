T = int(input())

arr = [2, 3, 5, 7, 11]

for tc in range(T):
  N = int(input())
  exp = [0] * 5

  for i in range(5):
    while N % arr[i] == 0:
      N //= arr[i]
      exp[i] += 1
  
  print(f"#{tc+1} {*exp}")