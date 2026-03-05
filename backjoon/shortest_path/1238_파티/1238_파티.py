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

for start in range(1, N+1): # 각 마을별로 헉생 개인의 시작지점을 정한다.
    # 갈때 다익스트라 돌리고
    # 반환값을 go_dist에 저장하고
    # print(f"{start}번 마을에서 시작!")
    # print(f"도착지는 {X+1}번 마을!")
    go_dist = dijkstra(start, N, adj)
    # print(go_dist)

    # 올떄 다익스트라 돌리고
    # 반환값을 come_dist에 저장하고
    come_dist = dijkstra(X, N, adj)
    # print(come_dist)
    # 단순히 같은 자리끼리 더하는게 아니라
    # 왔다 갔다 값을 더해야한다.
    tmp = go_dist[X] + come_dist[start]
    # print(tmp)
    # print()
    if max_dist < tmp:
        max_dist = tmp
print(max_dist)