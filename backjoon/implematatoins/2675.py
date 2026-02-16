test_case = int(input())
for i in range(test_case):
  result = ""

  repeat, text = input().split()
  # ABC, /HTP

  repeat = int(repeat)
  # 2
  text = list(text)
  # ['A', 'B', 'C']

  for j in range(len(text)):
    result += text[j] * repeat

  print(result)