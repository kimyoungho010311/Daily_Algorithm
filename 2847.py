# N 입력받기

# N 만큼 리스트 입력받기

# for 마지막 요소를 기준으로 N-1 번쨰 요소를 찾기
# 만약 N-1 >= N 이면
# [N-1] -1 and cnt += 1
# if [N-1] < N
#   [N-2] >= [N-1]


N = int(input())
arr =[]
cnt = 0
for _ in range(N):
  arr.append(int(input()))

for i in range(len(arr)-1, -1, -1):
  if i != 0:
    while True:
      if arr[i-1] >= arr[i]:
        #print(f"{arr[i-1]} >= {arr[i]} 이므로 {arr[i-1]}의 값을 1 뺴고 cnt += 1")
        arr[i-1] -= 1
        cnt += 1
      elif arr[i-1] < arr[i]:
        #print(f"{arr[i-1]} < {arr[i]}이므로 break하고 다음으로 넘어감")
        break
  else:
    print(cnt)