S = input()

ls_1 = S.split("0")
cnt_1 = 0
for i in range(len(ls_1)):
  if "1" in ls_1[i]:
    cnt_1 +=1

ls_0 = S.split("1")
cnt_0 = 0
for i in range(len(ls_0)):
  if "0" in ls_0[i]:
    cnt_0 +=1


if cnt_0 < cnt_1:
  print(cnt_0)
else:
  print(cnt_1)