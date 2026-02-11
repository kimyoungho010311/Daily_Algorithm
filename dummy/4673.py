has_generator = [False] * 10001 # [False]로 이루어진 리스트 생성

def d(n):
  result = n
  n_str = str(n)
  for digit in n_str:
    result += int(digit)
  return result

for i in range(1, 10001):
  generated_num = d(i)

  if generated_num <= 10000:
    has_generator[generated_num] = True

for i in range(1, 10001):
  if not has_generator[i]:
    print(i)