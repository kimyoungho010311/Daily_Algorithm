N = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = 0

arr1.sort()
arr2.sort(reverse=True)

for i in range(N):
  result += arr1[i] * arr2[i]

print(result)