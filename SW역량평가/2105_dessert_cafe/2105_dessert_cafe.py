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

# 오른쪽아래, 왼쪽아래, 왼쪽위, 오른쪽위
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def DFS(i, j, d):
    global max_ans

    # 이동 (직진 / 꺽기)
    # 현재 방향부터 다음 방향까지만 고려(사각형이므로 뒤로 갈 필요가 없다.)
    # 기존의 방식대로 4번을 반복한다면 이상한 모앙이 된다.
    # 하지만 d, d+1만 사용한다면 직진하고, 꺽고 밖에 없으므로 사각형이 만들어진다.
    
    for next_d in range(d, d + 2):
        if next_d < 4: # 다음 방향이 di, dj의 인덱스를 벗어나지 않도록 하는 안전장치
            ni, nj = i + di[next_d], j + dj[next_d]

            # 사각형 완성 체크 (마지막 방향에서 시작점으로 돌아온 경우)
            if ni == si and nj == sj: # 만약 다음 이동 지점이 시작지점이라면 사각형이 완성됬다고 판단한다.
                #if len(visited_cafe) >= 4:
                max_ans = max(max_ans, len(visited_cafe))
                return

            # 지도 안이고 안먹어본 디저트라면
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] not in visited_cafe:
                    visited_cafe.append(board[ni][nj])
                    DFS(ni, nj, next_d)
                    visited_cafe.pop() # 백트래킹 해줘야함

T = int(input())

for tc in range(1, T+1):
    # 지도의 크기
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_ans = -1 # 기본값으로 -1을 준다.

    for si in range(N-2): # 사각형 공간 확보를 위해 범위 제한
        for sj in range(1, N-1):
            visited_cafe = [board[si][sj]]
            DFS(si, sj, 0)
    print(f"#{tc} {max_ans}")
