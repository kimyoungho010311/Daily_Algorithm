import sys
sys.stdin = open('input.txt')

# 방향 정의 (상, 하, 좌, 우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
# 명령어와 인덱스 매핑
dir_map = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
tank_shapes = ['^', 'v', '<', '>']

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    orders = input()

    # 1. 초기 전차 위치 및 방향 찾기
    r, c, d = 0, 0, 0
    for i in range(H):
        for j in range(W):
            if board[i][j] in tank_shapes:
                r, c = i, j
                d = tank_shapes.index(board[i][j])
                break # 탱크 위치 찾았으면 이제 더 이상 탐색 필요없으니깐 중지

    # 2. 명령어 수행
    for order in orders:
        if order == 'S':
            # 포탄 발사
            sr, sc = r + di[d], c + dj[d]
            while 0 <= sr < H and 0 <= sc < W:
                if board[sr][sc] == '*':  # 벽돌 벽: 평지화 후 소멸
                    board[sr][sc] = '.'
                    break
                elif board[sr][sc] == '#':  # 강철 벽: 그냥 소멸
                    break
                sr += di[d] # d 에는 index값이 들어있다 즉 탱크가 바라보는 방향이 들어가 있다.
                sc += dj[d]
        else:
            # 이동 명령 (U, D, L, R)
            d = dir_map[order]  # 방향 전환
            board[r][c] = tank_shapes[d]
            nr, nc = r + di[d], c + dj[d]

            # 이동 가능 여부 체크 (범위 안 + 평지)
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.':
                board[r][c] = '.'  # 기존 자리 평지화
                r, c = nr, nc
                board[r][c] = tank_shapes[d]  # 새 자리 전차 배치

    # 3. 결과 출력
    print(f"#{tc}", end=" ")
    for row in board:
        print("".join(row))