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
adj = [[] for _ in range(N+1)] # 반드시 정점을 기준으로 인접리스트 생성!!!!!
max_dist = -1 # 정답

for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

# 다익스트라 알고리즘을 총 두번 돌려야할듯
# 갈때한번, 올떄한번
# 갈때 걸리는 시간 리스트, 올 때 걸리는 시간 리스트 두 개 만들어서
# 같은 자리 원소들끼리 합 한다음 max값 구하면 끝날듯
# 각 학생별로 모두 다익스트라 돌려야하나?

for start in range(1, N + 1):
    # 각 시작마을에서 파티 장소까지 가는 거리 구하기
    go_dist_list = dijkstra(start, N, adj)
    go_val = go_dist_list[X] # 파티장소까지 가는 거리

    come_dist_list = dijkstra(X, N, adj) # 집으로 돌아오는 거리
    come_val = come_dist_list[start]

    # 두 값을 더해 최댓값 갱신
    total_time = go_val + come_val
    if max_dist < total_time:
        max_dist = total_time

print(max_dist)