import sys
sys.stdin = open('input.txt')
"""
N*N형태로 이루어져 있으며 최장거리를 만들려고 한다.
각 칸의 숫자는 높이를 말한다.

규칙은 아래와 같다.
1. 가장 높은 봉우리에서 시작되어야 한다.
2. 반드시 높 -> 낮으로 가야한다. 상 하 좌 우 움직일 수 있따.
3. 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
====================================================

3번 조건은 음.. 완탐을 통해서 최장값 구하는거같음

일단 첫 번째로 주어진 배열에서 max 값을 찾아서 start 리스트에 추가해줘야 한다. 그런 다음에 각 시작점들 마다 DFS를 적용해서
가장 최장 거리를 구해본다.

이 문제의 가장 큰 걸림돌이 3번 조건이다.
모든 시작점에서 DFS를 적용해 최장거리를 구하는건 쉽다. 하지만 어떤 방법으로 K만큼 깎아서 최장거리를 만들어야하나?

K깎기 아이디어
딱 한곳을 잘라내야한다...
    
    1. 모든 곳을 이중 반복문으로 완탐하면서 K부터 시작하여 K=0이 될때까지 반복해보기
    이 방법은 8 * 8 * 5 = O(320)인데... 좀 빠르게 하면 가능할듯?
    
    2. ...
    
    
    
"""
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def DFS(i, j, h, dist, is_cut):
    global max_dist
    max_dist = max(max_dist, dist)

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # 그냥 내려갈 수 있는 경우
            if board[ni][nj] < h:
                visited[ni][nj] = True
                # 반드시 인자값을 is_cut을 넘겨줘야한다. False를 넘겨줄 경우 계속해서 새로 선언하는것이기 때문에
                # 플래그 변수가 작동하지 못한다.
                DFS(ni, nj, board[ni][nj], dist + 1, is_cut)
                visited[ni][nj] = False # 백트래킹

                # 공사 찬수가 남아 있고, 깎아서 나보다 낮아질 수 있는 경우
            elif not is_cut and board[ni][nj] - K < h:
                visited[ni][nj] = True
                # 최대한 덜 깍는게 유리하므로 나보다 딱 1 작게 만든다.
                DFS(ni, nj, h -1, dist + 1, True)
                visited[ni][nj] = False # 백트래킹

T = int(input())

for tc in range(1, T+1):
    # 보드판 크기, 자르는 수
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    # 시작지점은 가장 높은 봉우리이다.
    start_value = max(map(max, board))

    start_position = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == start_value:
                start_position.append((i, j))

    max_dist = 0
    # 각 지점들마다 DFS 알고리즘 적용해보기
    for start in start_position:
        i, j = start
        visited[i][j] = True
        # 현재 좌표, 현재 높이, 지금까지 걸어온 거리, 공사를 이미 했는지 여부
        DFS(i, j, board[i][j], 1, False)
        visited[i][j] = False
    # 위에 방식처럼 각 시작지점마다 DFS를 적용하는게 아니라
    # 아 뭔가.. 무지성으로 K를 하나씩 줄여가면서 산을 깎는게 아니라 조건에 만족하면 1씩 더 줄여나가보기 해봐야 할거같음

    print(f"#{tc} {max_dist}")