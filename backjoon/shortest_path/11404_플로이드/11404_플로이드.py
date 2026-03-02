import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

def floyd_warshall(N, graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

N = int(input())  # 도시 수
M = int(input())  # 버스 수

INF = float('inf')
graph = [[INF] * N for _ in range(N)]

# 자기 자신으로 가는 비용 0
for i in range(N):
    graph[i][i] = 0

# 간선 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

result = floyd_warshall(N, graph)

# 출력 (도달 불가 = 0)
for i in range(N):
    for j in range(N):
        if result[i][j] == INF:
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()