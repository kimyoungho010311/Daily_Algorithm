T = int(input())

for tc in range(T):
  N, M = map(int, input().split())
  arr1 = set(input().split())
  arr2 = set(input().split())

  result = len(arr1 & arr2)

  print(f"#{tc+1} {result}")