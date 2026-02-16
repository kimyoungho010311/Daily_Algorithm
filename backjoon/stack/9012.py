import sys

t = int(sys.stdin.readline())

for _ in range(t):
  stack = []
  s = sys.stdin.readline().strip()

  for ch in s:
    if ch == '(':
      stack.append(ch)
      # print(stack)
    else:
      if len(stack) == 0:
        print("NO")
        break
      else:
        stack.pop()
        # print(stack)
  else:
    if len(stack) == 0:
      print("YES")
    else:
      print("NO")
