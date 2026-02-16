import sys

t = int(sys.stdin.readline())
stack = []

for _ in range(t):
  o = sys.stdin.readline().split()

  if o[0] == "push":
    stack.append(o[1])

  elif o[0] == 'pop':
    if not stack:
      print("-1")
    else:
      print(stack.pop())

  elif o[0] == "size":
    print(len(stack))

  elif o[0] == "empty":
    if not stack:
      print("1")
    else:
      print('0')
  
  elif o[0] == 'top':
    if not stack:
      print("-1")
    else:
      print(stack[-1])