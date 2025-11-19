for tc in range(1, 10):
  N = int(input())

  res = 0
  exp = input()

  for i in range(len(exp)):
    if exp[i].isdigit():
      sum += exp[i]

    print(f"#{tc} {sum}")