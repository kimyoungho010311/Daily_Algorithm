import sys
sys.stdin = open('input.txt')
"""
모든 행성을 연결하면서 최소 관리 비용으로 할려고 한다.

N개의 행성으로 표시하고 행성 i, j 관리 비용은 Cij이다.
모든 행성을 연결하고 최소 유지비용을 구하자.
"""
import sys
input = sys.stdin.readline

# 행성의 수
N = int(input())

# adj_list 생성
adj_list = [list(map(int, input().split())) for _ in range(N)]

selected = [False] * N
min_edge = [float('inf')] * N

min_edge[0] = 0 # 시작 정점
result = 0

for _ in range(N):
    u = -1
    min_val = float('inf')

    # 아직 선택되지 않은 정점 중 최소 간선 선택
    for i in range(N):
        if not selected[i] and min_edge[i] < min_val:
            min_val = min_edge[i]
            u = i
    selected[u] = True
    result += min_val

    # 선택된 정점을 통해 min_edge 갱신
    for v in range(N):
        if not selected[v] and adj_list[u][v] != 0:
            if adj_list[u][v] < min_edge[v]:
                min_edge[v] = adj_list[u][v]

print(result)