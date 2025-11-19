t = int(input())


for tc in range(t):
  N, M, L = map(int, input().split())
  # N : 첫 수열의 길이
  # M : 추가 횟수
  # L : 출력할 인데스 번호

  arr = list(map(int, input().split()))

  for i in range(M):
    index, value = map(int, input().split())
    arr.insert(index, value)

  print(f"#{tc+1} {arr[L]}")