import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)
input = sys.stdin.readline
"""
그냥 테트리스 아닌가

1. 정사각형은 서로 겹치면 안된다.
2. 도형은 모두 연결되어야 한다.
3. 정사각형의 변끼리 연결되어야 한다. 꼭짓점 끼리 연결은 ㄴ

정사각형 4개를 이어야한다. 총 5가지의 모형이있다.

아름이는 N*M 위에 테트로미노 하나를 놓으려고 한다.
각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 완성해라

모든 블록들(ㅗ 제외)은 한붓그리기로 이루어져 있다.
즉, DFS의 깊이를 4번까지 제한하면 도형이 그려지고, 회전 반전로직도 해결된다.

어째서 백트래킹이 필요한가?
나는 한 지점에서 모든 모양의 방향으로 계속해서탐색해야 한다.
하지만 방문지점에 표시가 되어 있을 경우 다음 칸으로 넘어가기 때문에
방문했던 흔적을 지워 1번 모양의 탐색을 완료했으면 2번 모양을 탐색한다.
이런 이유로 백트래킹이 필요하다.
"""

def dfs(r, c, depth, total):
    global result

    # 가지치기: 현재 합 + (남은 칸 * 전체 최댓값) <= 현재 최고점이면
    # 앞으로 가망이 없으므로 빨리 종료해버린다.
    if total + max_val * (4 - depth) <= result:
        return

    if depth == 4:
        result = max(result, total)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True # 방문 처리 하고
            dfs(nr, nc, depth + 1, total + board[nr][nc]) # 다음 칸 가보고
            visited[nr][nc] = False # 백트래킹을 위해 되돌린다.

# ㅗ, ㅜ, ㅏ, ㅓ 모양을 별도로 체크하는 함수
def check_t_shape(r, c):
    global result
    for i in range(4):
        # 4방향 중 하나를 제외한 3방향 + 중심점 = 4칸
        temp_sum = board[r][c] # 임시로 가운데 칸을 선정한 다음
        is_valid = True
        for j in range(4):
            # i번째 방향만 빼고 나머지 3방향 더하기
            # 십자가 모양으로 퍼지는데 한쪽만 안간다는 마인드
            if i == j: continue

            nr, nc = r + dr[j], c + dc[j]
            if 0 <= nr < N and 0 <= nc < M:
                temp_sum += board[nr][nc]
            else:
                # 한칸이라도 보드 밖을 나가면 불합격
                is_valid = False
                break # 바로 정지한다.
        # 모든 검사가끝난 후 True일 경우에만 최댓값 비교를 한다.
        if is_valid:
            result = max(result, temp_sum)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_val = max(map(max, board))
result = 0

for r in range(N):
    for c in range(M):
        # 1. 일반 DFS (I, O, L, S 모양)
        # 아래 방법이 백트래킹 방법이라고 한다.
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False

        # 2. ㅗ 모양 체크
        check_t_shape(r, c)

print(result)