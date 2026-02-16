# 620

# 500 1
# 100 1
# 50 0
# 10 2
# 5 0
# 1 0
# ----------
# 4개

# 999
# 500 1
# 100 4
# 50 1
# 10 4
# 5 1
# 1 4
# -----------
# 15개

ori = 1000 # 상점이 가진 돈
coin = [500, 100, 50, 10, 5, 1]
result = 0 # 거스름돈 갯수

input = int(input()) # 백준이가 준 돈
sub = ori - input # 거스름돈
#print(sub)
for i in range(len(coin)):
  result += sub // coin[i]
  #print(f"sub % coin{i} = {result}")
  sub = sub % coin[i]
  #print(f"sub // coin{i} = {sub}")
print(result)

# print(999 % 500)
# print(999 // 500)