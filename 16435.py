N, L = map(int, input().split())
arr = list(map(int, input().split(" ")))
arr.sort()
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(arr)):
  if arr[i] <= L:
    L+=1
  else:
    break

print(L)