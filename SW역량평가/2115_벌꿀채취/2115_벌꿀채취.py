import sys
sys.stdin = open('input.txt')
""""
N*N 모양의 벌통이 배치되어있다.
각 칸에는 꿀의 양을 나타내며 서로 다를 수 있다.

반드시 가로로 연속도록 연속으로 M개를 골라야한다.
겹치는 부분은 없어야한다. ( 백트래킹 )

총 두명이서 벌꿀을 채취한다.
각각 M개의 연속된 가로방향으로 꿀을 채취해야하고
총 두개의 꿀통에 나눠 담아야한다.

만약 꿀통의 크기보다 커지면 최대한 많이 담아야한다.
여기서 이제 최대 수익을 구하ㅐ서 어쩌구 저꺼구 쏼라쏼라
=========================================================
슬라이딩 윈도우, 이중포문으로 완탐, 그리디, 가지치기, 백트래킹

이동방향이 정해져있어서 visited는 필요없을거같다.
만약 m=2면 크기가 2인 윈도우를 계속해서 슬라이딩으로 움직여주는것으로 한다.

이중반복문으로 각각 다 비교를 해준다.
만약 중간에 어떤 비교 로직을 활용해서 가망이 없을거같으면 바로 다음 반복으로 continue한다.

꿀 채취하는 한명이 골랐을때 거기서 최대한 C에 인접한 최댓값을 어떻게 구해야할까...

일단 정렬한다음 합계를 구한다.
그 다음 채취 리스트를 하나씩 돌라아가면서 빼다보면 ㅇC보다 작아지는 순간이 온다.. 그떄 연산을 멈추면 그때값이 꿀통에 들어가는 최댓값이다.

이런식으로 하면 될듯 ㅋㅋ!
"""

T = int(input())

def get_profit(honey_list, limit_C):
    # 특정 꿀통 묶음(M개)에서 얻을 수 있는 최대 수익 계산
    # 이 함수 안에서만 쓸 최댓값 변수
    max_p = 0
    m = len(honey_list)

    def dfs(idx, current_sum, current_profit):
        nonlocal max_p # 외부 변수인 max_p를 수정하기 위해 사용

        # 모든 꿀을 다 확인했을 때
        if idx == m:
            max_p = max(max_p, current_profit)
            return

        # 현재 꿀을 담는 경우 (limit_C를 안넘길때만)
        if current_sum + honey_list[idx] <= limit_C:
            dfs(idx + 1, current_sum + honey_list[idx], current_profit + (honey_list[idx]**2))

        # 현재 꿀을 담지 않는 경우
        dfs(idx + 1, current_sum, current_profit)

    # DFS 시작
    dfs(0, 0, 0)
    return max_p

for tc in range(1, T+1):
    # 벌통들의 크기, 선택 가능한 벌통 수, 채취가능한 최대 양
    N, M, C = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    # profit_map[r][c] = (r, c)부터 가로로 M개 선택했을 떄의 수익
    profit_map = [[0] * N for _ in range(N)]
    for r in range(0, N):
        for c in range(0, N-M+1):
            honey_list = board[r][c:c+M]
            profit_map[r][c] = get_profit(honey_list, C)

    # 두 명의 일꾼에게 꿀통 배정
    max_total_revenue = 0
    for r1 in range(0, N):
        for c1 in range(0, N-M+1):
            ans_A = profit_map[r1][c1]

            # 일꾼 B의 시작 지점
            for r2 in range(0, N):
                for c2 in range(0, N-M+1):
                    # A와 B가 같은 줄일 때
                    if r1 == r2:
                        # B가 A보다 뒤에 있고, M만큼 떨어져 있어야 안겹침
                        if c2 >= c1 + M:
                            max_total_revenue = max(max_total_revenue, ans_A + profit_map[r2][c2])

                    # A와 B가 다른 줄일 때
                    elif r1 < r2: # 중복 계산 방지를 위해 r2가 클 때만 체크
                        max_total_revenue = max(max_total_revenue, ans_A + profit_map[r2][c2])

    print(f"#{tc} {max_total_revenue}")