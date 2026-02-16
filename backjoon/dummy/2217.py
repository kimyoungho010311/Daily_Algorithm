n = int(input())
k = []

for _ in range(n):
  k.append(int(input()))
k.sort() # 10 15

ans = []

for x in k:
  ans.append(x*n)
  n -=1
print(max(ans))