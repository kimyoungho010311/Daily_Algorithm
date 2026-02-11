# 숫자 입력받고
N = list(input())
N.sort(reverse=True)
res = ""
# 리스트[ㅋ] 의 숫자가 30의 배수이면 배수 리스트에 입력

for i in range(len(N)):
  res+=N[i]

if int(res) % 30 == 0:
  print(res)
else:
  print(-1)