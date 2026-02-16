import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

'''
M, N, K: 세로, 가로, 직사각형의 수 (M,N <=100)

K의 크기를 어떻게 구해야하나
-> 아마 M, N 은 좌표를 뜻하니 항상 양수이다... (뭔말이여)
'''

def make_k_square(sx, sy, ex, ey, mat):
    # 이중 반복문으로 어케 가능할거같은데
    for i in range(sy, ey): #Y의 길이만큼
        for j in range(sx, ex): #X의 길이만큼
            # print(f"(x, y) = ({i}, {j})")
            mat[i][j] = 1
    return

def DFS(i, j):

    mat[i][j] = 1
    cnt = 1
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < M and 0 <= nj < N and mat[ni][nj] == 0:
            cnt += DFS(ni, nj) # 이런식으로 반환값 을 더해야 빈곳의 크기를 구할 수 있다. -> 섬 크기 찾는 문제에서도 활용 가능할 듯
    return cnt


M, N, K = map(int, input().split()) # 5, 7, 3
# 0이 방문 가능한 곳
# 1이 방문 불가능한 곳
mat = [[0] * N for _ in range(M)]
answer = []
number_of_square = 0
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split()) # [(0, 2, 4, 4), (1, 1, 2, 5), (4, 0, 6, 2)]
    make_k_square(sx, sy, ex, ey, mat)

for i in range(M):
    for j in range(N):
        if mat[i][j] == 0:
            number_of_square += 1 # 0인곳을 찾았다면 그곳을 기점으로 빈 공간을 카운팅한다.
            answer.append(DFS(i, j)) # 이제 상하좌우를 기준으로 모두 1로 변경한다. (방문 표시를 한다.)

answer.sort()
print(number_of_square)
print(*answer)
