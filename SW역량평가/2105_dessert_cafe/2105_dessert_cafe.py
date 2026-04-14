import sys
sys.stdin = open('input.txt')
"""
N * N에 디저트 카페가 모여져있다.

각 칸에 숫자는 카페에서 판매하는 디저트의 종류를 의미하고 가페들 사이에는 대각선으로 움직일 수 가 있다.
대각선 방향으로 투어하고 반드시 원래 방향으로 돌아와야 한다. 또한 방문했던 곳은 다신 방문하지 않는다.
즉 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안된다.

디저트를 최대한 많이 먹으려고 한다.
임의의 한 카페에서 출발하여 대각선으로만 움직이고, 서로 다른 디저트를 먹으면서
사각형 모양을 그리고 다시 출발점으로 돌아오는 경우
디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 떄의 디저트 수를 출력해라.
만약 디저트를 먹을 수 있는 경우가 없다면 -1 을 출력한다.

여기까지가 문제 정리... 아래는 예상 풀이

델타탐색을 사용한다 이동방향은 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래 4방향이다.
시작점은 주어지지 않는다. 즉, 주어진 지도를 완탐 하면서 DFS 알고리즘을 적용해야한다.

for i in range(N):
    for j in range(N):
        is_vaild = False # 해당 지점에서 조건에 만족하는 카페 리스트를 만들 수 있는지 검사한다.
        max_ans = max(max_ans ,DFS(i, j))
        

def DFS(i, j):
    global is_vaild
    ni, nj = 알아서 구하고(대각선 방향)
    
    만약 ni, nj이 초기에 입력받았던 시작지점이라면 사각형이 만들어졌다고 판단하고
        retrun visited_cafe # 바로 함수를 종료한다.
        
    만약 다음 지점이 지도에 있고 방문한 적이 없다면:
        visited_cafe.append(board[i][j]) 를 추가하여 방문했던 리스트에 추가한다.
    
    return if len(visited_cafe) > 0 visited_cafe else: -1
"""

# 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
di = [-1, -1, 1, 1]
dj = [-1, 1, -1, 1]

def DFS(i, j):
    global visited_cafe

    goal_i, goal_j = i, j # 다시 돌아와야 하는 목적지
    visited[i][j] = True

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if ni == goal_i and nj == goal_j: # 목적지에 다시 돌아왔음으로 DFS를 반환한다.
            return visited_cafe

        # 지도 안에 있어야 하고 방문한 적이 없고 똑같은 메뉴가 아니라면
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and board[ni][nj] not in visited_cafe:
            visited_cafe.append(board[ni][nj])
            DFS(ni, nj)
    return len(visited_cafe) if visited_cafe else -1

T = int(input())
T = 1
for tc in range(1, T+1):

    # 지도의 크기
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    max_ans = -1 # 기본값으로 -1을 준다.

    for si in range(N):
        for sj in range(N):
            # is_valid = False # 최종 형태가 사각형인지 확인한다. 이거 쓸모있나
            # 방문했던 카페 리스트
            visited_cafe = []
            visited_cafe.append(board[si][sj])
            tmp_ans = DFS(si, sj)
            max_ans = max(max_ans, tmp_ans)

    print(f"#{tc} {max_ans}")
