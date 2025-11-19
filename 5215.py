T = int(input())

for tc in range(1, T+1):
  N, L = map(int, input().split())
  items = []

for _ in range(N):
  t, k = map(int, input().split())
  items.append((t, k))
print(items)

best = 0

def dfs(i, score, cal):
    global best 
    if cal > L:# 칼로리가 최대치를 넘으면 종료
        return
    if i == N: # N : 최대 음식애 갯수에 도달하면
        if score > best: 
            best = score
        return

    dfs(i+1, score + items[i][0], cal + items[i][1])
    dfs(i+1, score, cal)

dfs(0, 0, 0)
print(f"#{tc} {best}")