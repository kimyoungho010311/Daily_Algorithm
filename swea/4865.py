t = int(input())

for tc in range(t):
  str1 = list(input())
  str2 = input()
  
  max = 0

  for i in range(len(str1)):
    
    tmp = str2.count(str1[i])
    if tmp > max:
      max = tmp
  
  print(f"#{tc+1} {max}")
    