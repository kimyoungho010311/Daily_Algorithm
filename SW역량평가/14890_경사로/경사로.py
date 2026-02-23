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

# 지도의 크기, 경사로 길이
N, L = map(int, input().split()) # 6 2

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 길의 개수

# 일단 완전 탐색으로 해야 할 듯
# 행탐색, 열탐색 각각 두번 해야한다.
# 1. 모든 경사로의 높이가 같은 경우
# 1번같은 경우에는 curr 와 next 계속 비교해가면서 같으면 +=1 하고
# 다를 경우 break 걸고 경사로 로직 적용해봐야 할듯

for idx in range(N): # 가로 탐색
    tmp = arr[idx:][0]
    print(tmp)
    # 뭔가 이 반복문이 문제인거같아 개선점이 필요함 정확히 내가 원하는대로 이 반복문을 탈출하고싶은데.. 플래그 변수를 사용해야하나
    for index in range(len(tmp)-1):
        curr_elem = tmp[index]
        next_elem = tmp[index+1]

        # curr와 next가 다른게 있으면 차이를 검사하고
        # 만약 차가 1이라면 그곳에 L길이의 경사로가 들어가는지 로직을 검사한다.
        # 경사로가 들어가는 공간이 없으면 그냥 pass
        if curr_elem != next_elem:
            diff = abs(curr_elem - next_elem)
            print(diff)


        # 만약 끝까지 순회했다면 경사로가 필요 없으므로
        # 최종 결과에 += 1한다.


print()
# 세로 탐색 하기 위해서 배열을 90도 회전한다.
arr = [list(row) for row in zip(*arr[::-1])]

for idx in range(N):
    tmp = arr[idx:][0]
    pass