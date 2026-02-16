T = int(input())

for tc in range(T):
  a, b = map(int,input().split())
  
  if 10 <= a or 10 <= b:
    print(f"#{tc+1} -1")
  else:
    result = a * b
    print(f"#{tc+1} {result}")