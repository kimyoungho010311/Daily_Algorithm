import sys
sys.stdin = open('input.txt')
'''
N * N 크기의 도시가 있다. 각 도시는 빈칸 치킨집, 집 중 하나이다.
(r, c)으로 나타내지고 r행 c열

치킨 거리: 집과 가장 가까운 치킨집 사이의 거리이다.
각 집별로 치킨거리가 있다.
도시의 치킨 거리 = all(치킨거리)
====================================================================================================
최대 M개를 고르고 나머지는 모두 폐업시켜야한다. 어떻게 고르면 **도시의 치킨 거리**가 최소가 되는지 구해라
일단 DFS로 각 집의 치킨 거리를 구한다음에 도시의 치킨 거리를 구한다.
도시의 치킨 거리를 구하는데 사용되지 않은 치킨집은 일단 폐업시키고 ( 탐색에 사용된 치킨집은 3으로 봐꿔본다. -> 이러면 따로 저장 안해도 되서 좋음 )
만약 그래도 더 폐업 시켜야한다면 순열로 풀어보면 별로 안걸릴거같다.
시간 초과도 안난다.

시작지점을 완탐으로 하지말고 집(1)에서 시작한다.
만약 치킨집(2)에 도착하면 바로 멈춘다.
'''
# def DFS(i, j, depth):
#     if city[i][j] == 2 or city[i][j] == 3: # 치킨집에 도착하면 정지
#         # city[i][j] = 3
#         print(f"{i}, {j}에 도착했습")
#         return depth
#
#     for k in range(4):
#         ni, nj = i + di[k], j + dj[k]
#
#         if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
#             visited[ni][nj] = True
#             DFS(ni, nj, depth + 1)
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = {}
chicken = []

# 1. 집과 치킨집 위치 파악
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house[(i, j)] = []  # 집의 좌표를 키로 설정
        elif city[i][j] == 2:
            chicken.append((i, j))  # 치킨집 좌표 저장

# 2. 각 집에서 '모든' 치킨집까지의 거리 미리 계산하여 저장
# chicken 리스트의 인덱스가 house[h] 리스트의 인덱스와 매칭됩니다.
for h in house:
    hi, hj = h
    for ci, cj in chicken:
        dist = abs(hi - ci) + abs(hj - cj)
        house[h].append(dist)

# 3. M개의 치킨집을 고르는 모든 경우의 수 탐색
# chicken_indices는 0부터 (전체 치킨집 개수-1)까지의 인덱스 번호입니다.
chicken_indices = list(range(len(chicken)))
min_city_chicken_dist = float('inf')

# itertools.combinations를 사용해 M개를 뽑는 인덱스 조합을 생성
for selected_indices in combinations(chicken_indices, M):
    current_city_dist = 0

    # 각 집마다 선택된 치킨집들 중 최소 거리를 계산
    for h in house:
        # house[h]에는 모든 치킨집과의 거리가 들어있으므로,
        # 선택된 인덱스(selected_indices)에 해당하는 거리들만 확인합니다.
        distances_to_selected = [house[h][idx] for idx in selected_indices]
        current_city_dist += min(distances_to_selected)

    # 도시의 치킨 거리 최솟값 갱신
    if current_city_dist < min_city_chicken_dist:
        min_city_chicken_dist = current_city_dist

print(min_city_chicken_dist)
