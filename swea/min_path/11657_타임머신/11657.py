import sys
sys.stdin = open('input.txt')
"""
음수 가중치가 있다.
Bellman-Frod 알고리즘
"""
# 여기 아래에 코드 ㄱㄱ

input = sys.stdin.readline

# 도시(노드), 버스(간선)
N, M = map(int, input().split())
edges = []

for _ in range(M):
    edges.append(list(map(int, input().split())))


INF = float('inf')
# 한 시작점을 위치로 하므로 1차원 리스트를 사용한다.
dist = [INF] * (N + 1)
start_node = 1
# 출발 노드는 0, 나머지 노드는 모두 무한대로 초기화한다.
dist[start_node] = 0

has_negative_cycle = False

# 모든 간선을 하나씩 확인하며 검사한다.
for i in range(N):
    for s, e, weight in edges:
        # 현재 간선을 거쳐서 가는게 더 빠르다면 갱신한다.
        if dist[s] != INF and dist[e] > dist[s] + weight:
            dist[e] = dist[s] + weight

            # 음수 사이클 체크
            if i == N - 1:
                has_negative_cycle = True

# 결과 출력
if has_negative_cycle:
    # 시간을 무한히 되돌릴 수 있는 경우
    print("-1")
else:
    # 2번 도시부터 N번 도시까지 가는 가장 빠른 시간 출력
    for i in range(2, N + 1):
        if dist[i] == INF:
            # 경로가 없는 경우
            print("-1")
        else:
            print(dist[i])