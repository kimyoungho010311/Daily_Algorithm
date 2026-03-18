import sys
sys.stdin = open('input.txt')

def dfs(i, j, depth, total):
    global result

    if total + max_val * (4 - depth) <= result:
        return

    if depth == 4:
        result = max(result, total)
        return

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, depth + 1, total + board[ni][nj])
            visited[ni][nj] = False

def check_t_shape(i, j):
    global result

    for k in range(4):
        tmp_sum = board[i][j]
        is_valid = True

        for m in range(4):
            if k == m: continue

            ni, nj = i + di[m], j + dj[m]
            if 0 <= ni < N and 0 <= nj < M:
                tmp_sum += board[ni][nj]
            else:
                is_valid = False
                break
        if is_valid:
            result = max(result, tmp_sum)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

result = 0
max_val = max(map(max, board))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])

        check_t_shape(i, j)

        visited[i][j] = False

print(result)