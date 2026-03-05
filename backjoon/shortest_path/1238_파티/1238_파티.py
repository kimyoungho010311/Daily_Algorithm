import sys, heapq
sys.stdin = open('input.txt')
"""
N개로 구분된 마을에 한 명의 학생이 있다.
N명의 학생이 X번 마을에 모여 파티를 벌인다.
마을 사이에는 M개의 단방향 도로들이 있고 Ti만큼 시간을 소비한다.
각각의 학생들은 파티에 참석하고 다시 돌아와야한다.
단방향이기때문에 가고 오는데 길이 다를 수 도 있다.
N명의 학생들 중 가장 많은 시간을  소비하는 학생은?
"""
input = sys.stdin.readline

def dijkstra(start, N, adj):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq,(0, start))

    while pq:
        curr_acc, curr = heapq.heappop(pq)

        if curr_acc > dist[curr]:
            continue

        for next_v, weight in adj[curr]:
            cost = curr_acc + weight

            if dist[next_v] > cost: # 반드시 next_v!!!!!
                dist[next_v] = cost
                heapq.heappush(pq,(cost, next_v))
    return dist

# 마을 수, 길, 목적지 마을
N, M, X = map(int, input().split())
# 정방향 그래프 (X에서 집으로 돌아올 때 사용)
adj = [[] for _ in range(N+1)] # 반드시 정점을 기준으로 인접리스트 생성!!!!!
# 역방향 그래프 (집에서 X로 갈 때 사용)
rev_adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))
    rev_adj[e].append((s, w))

# X에서 각 마을로 돌아오는 최단 거리
come_dist = dijkstra(X, N, adj)

# 각 마을에서 X로 가는 최단 거리
go_dist = dijkstra(X, N, rev_adj)

# 오고 가는 시간의 합 중 최댓ㄱ밧 찾기
max_total_time = 0
for i in range(1, N+1):
    total = go_dist[i] + come_dist[i]
    max_total_time = max(max_total_time, total)

print(max_total_time)

