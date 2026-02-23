import sys
sys.stdin = open('input.txt')
"""
N * N 크기의 지도
지나갈 수 있는 길이 몇개가 있는지 알아본다.

길이란?
행 / 열 전부를 뜻하며 첨부터 끝까지 지나가는 것을 말한다.

길을 지나갈 수 있으며련 모든 칸의 높이가 같아야한다.
경사로도 가능하며 높이는 항상 1, 길이는 L이다. 개수는 무한

경사로는 높은칸 <-> 낮은칸을 이어준다.

조건들
1. 경사로는 낮은칸에 놓고, 바닥면이 모두 닿아야한다.
2. 낮은 칸과 높은 칸의 높이 차이는 1이어야한다.
3. 경사로를 놓은 낮은 칸의 높이는 모두 같아야하고, L개의 칸이 연속되어야 한다.

불가능한 경우
1. 경사로 위에 경사로
2. 낮은 칸 높은 칸 차이가 1이 아닌 경우
3. 낮은 지점의 칸이 높낮이가 다르고 길이가 L이 아닌 경우
4. **경사로가 범위를** 벗어나는 경우
"""
def check_line(line, N, L):
    """
    하나의 길을 받아서 지나갈 수 있는지 Boolean 값을 반환
    """

    # 경사로 설치 여부를 기록 ( 중복 설치 방지 ) <- 이게 왜 필요하지
    used = [False] * N

    for i in range(N-1):
        # 높이가 같은 경우 계속 전진
        if line[i] == line[i+1]:
            continue

        # 높이 차이가 1보다 큰 경우 -> 어떤 경우에도 불가능
        if abs(line[i] - line[i+1]) > 1:
            return False

        # 오르막길 (현재 < 다음) -> 지나온 길에 경사로 설치한다.
        if line[i] < line[i+1]:
            # 현재 칸(i)를 포함하여 왼쪽으로 L칸 확인
            for j in range(L):
                # 범위를 벗어나거나, 높이가 다르거나, 이미 경사로가 있다면
                if i - j < 0 or line[i] != line[i-j] or used[i-j]:
                    return False
                used[i-j] = True # 경사로 설치

        # 내리막길 (현재 > 다음) -> 앞으로 올 길에 설치한다.
        else:
            # 다음 칸을 포함하여 오른쪽으로 L칸 확인
            for j in range(1, L + 1):
                if i + j >= N or line[i+1] != line[i +j] or used[i+j]:
                    return False
                used[i+j] = True
    return True

# 지도의 크기, 경사로 길이
N, L = map(int, input().split()) # 6 2

board = [list(map(int, input().split())) for _ in range(N)]

ans = 0 # 길의 개수

# 일단 완전 탐색으로 해야 할 듯
# 행탐색, 열탐색 각각 두번 해야한다.
# 1. 모든 경사로의 높이가 같은 경우
# 1번같은 경우에는 curr 와 next 계속 비교해가면서 같으면 +=1 하고
# 다를 경우 break 걸고 경사로 로직 적용해봐야 할듯

for row in board:
    if check_line(row, N, L):
        ans += 1

# 세로 탐색 하기 위해서 배열을 90도 회전한다.
for col in zip(*board):
    if check_line(col, N, L):
        ans += 1

print(ans)