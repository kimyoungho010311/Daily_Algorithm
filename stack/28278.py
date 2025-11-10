import sys

t = int(sys.stdin.readline())
stack = []

for _ in range(t):
  order = sys.stdin.readline().split()
  #print(order)
  # print(f"ORDER : {order}")
    
  if order[0] == '1': #push
    #print(order[1])
    #print(f"APPEND! : {stack}")
    stack.append(order[1])
  
  elif order[0] == '2': #pop
    if not stack: # 비어있으면?
      print("-1")
    else:
      print(stack.pop())
  
  elif order[0] == '3':
    print(len(stack))
  
  elif order[0] == '4':
    if not stack:
      print("1")
    else:
      print("0")
  
  elif order[0] == '5':
    if stack:
      print(stack[-1])
    else:
      print("-1")