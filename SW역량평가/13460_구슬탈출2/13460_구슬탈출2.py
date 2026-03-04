import sys
from collections import deque

sys.stdin = open('input.txt')
"""
구슬탈출 보드게임은 빨간, 파란구슬을 하나씩 넣고, 빨간 구슬을 빼내는 게임

크키: N(세로) * M(가로)
벽은 모두 막혀있고, 구멍이 하나 존재
파란 구슬이 구멍에서 빠져나오면 안된다.

구슬은 기울려서 상 하 좌 우 움직이는게 가능하다.

공은 동시에 움직인다.
두 공은 같은 곳에 존재 불가능하다.
더 이상 공이 안움직이면 기울이기를 그만한다.

기울이면 벽을 만날때까지 간다.
"""
def solve():
    # 이 문제는 4차원 BFS에 대한 문제이다.
    
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    # 4차원 방문 리스트: visited[ri][rj][bi][bj]
    # 빨강(ri, rj)과 파랑(bi, bj)의 위치 조합을 방문 처리함
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = deque()
    ri, rj, bi, bj = 0, 0, 0, 0

    # 빨강, 파랑 구슬 위치 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                ri, rj = i, j
            elif board[i][j] == 'B':
                bi, bj = i, j

    # 큐에 (빨강i, 빨강j, 파랑i, 파랑j, 시도횟수) 삽입
    q.append((ri, rj, bi, bj, 1))
    visited[ri][rj][bi][bj] = True

    # 2. 구슬을 굴리는 함수 (벽이나 구멍을 만날 때까지)
    def move(i, j, mi, mj):
        '''
        parms:
            i: start i
            j: start j
            mi, mj: 구슬을 굴릴 방향
        return:
            i: end i
            j: end j
            count: 구슬이 움직인 거리를 반환한다.
        '''
        count = 0
        # 다음 칸이 벽이 아니고, 현재 칸이 구멍이 아닐 때까지 계속 이동
        while board[i + mi][j + mj] != '#' and board[i][j] != 'O':
            i += mi
            j += mj
            count += 1
        return i, j, count

    # 3. BFS 시작
    while q:
        ri, rj, bi, bj, dist = q.popleft()

        # 10번 넘게 시도하면 실패
        if dist > 10: # dist가 11번이 되는 순간 break
            break

        for k in range(4):
            # 각각의 구슬을 현재 방향으로 끝까지 굴림
            nri, nrj, r_cnt = move(ri, rj, di[k], dj[k])
            nbi, nbj, b_cnt = move(bi, bj, di[k], dj[k])

            # 파란 구슬이 구멍에 빠지면 실패 (이 방향은 무시)
            # 어째서 continue하면 이 방향 무시가 되는거지
            if board[nbi][nbj] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공!
            if board[nri][nrj] == 'O':
                print(dist)
                return

            # 두 구슬이 겹쳤을 때 처리 (가장 중요!)
            if nri == nbi and nrj == nbj:
                # 더 많이 이동한 구슬이 더 뒤에 있었다는 뜻이므로 한 칸 뒤로 뺌
                if r_cnt > b_cnt:
                    nri -= di[k]
                    nrj -= dj[k]
                else:
                    nbi -= di[k]
                    nbj -= dj[k]

            # 처음 가보는 위치 조합이라면 큐에 추가
            if not visited[nri][nrj][nbi][nbj]:
                visited[nri][nrj][nbi][nbj] = True
                q.append((nri, nrj, nbi, nbj, dist + 1))

    print(-1)  # 10번 안에 못 찾으면 -1
solve()




















