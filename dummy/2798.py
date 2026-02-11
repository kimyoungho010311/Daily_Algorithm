# N 장을 바닥에 숫자가 보이도록 세팅
# 딜러가 숫자 M을 말함

# 플레이어는 N장중 세장을 고름 (최대한 M과 비슷하도록)

N, M = map(int, input().split())
sum = 0
max = 0

nums = list(map(int,input().split()))
len_of_nums = len(nums)

for i in range(len_of_nums):
  for j in range(i+1, len_of_nums):
    for k in range(j+1, len_of_nums):
      sum = nums[i] + nums[j] + nums[k]
      print(f"{nums[i]} + {nums[j]} + {nums[k]} = {sum}") 

      if sum > max and sum <= M:
        max = sum

print(f"{max}")
