tx = input().upper()
tx_list = list(set(tx))
cnt = []

for i in tx_list:
  count = tx.count(i)
  cnt.append(count)

if cnt.count(max(cnt)) >= 2:
  print("?")
else:
  print(tx_list[cnt.index(max(cnt))])