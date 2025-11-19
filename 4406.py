#print(list.index("a"))

T = int(input())
target = ['a','e','i','o','u']
remove = [] # 지워야 하는 문자의 위치를 담는 리스트

for tc in range(T):
  text = list(input())
  
  for i in range(len(target)):
    if target[i] in text:
      remove.append(text.index(target[i]))
                    
  for j in range(len(remove)):
    text.pop(remove[j])

  print(f"#{tc+1} {''.join(text)}")
