import sys
sys.stdin = open('input.txt')
"""
N개의 정점, M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서 최장 경로의 길이를 계산

정점 1 ~ N번까지 구성
경로의 길이는 경로 상에 등장하는 정점상의 개수를 말한다.
"""
def DFS(curr, length):
    global ans

    ans = max(ans, length)

    for next_node in adj_list[curr]:
        if not visited[next_node]:
            visited[next_node] = True
            DFS(next_node, length + 1)
            visited[next_node] = False

T = int(input())

for tc in range(1, T+1):
    # 정점 수, 간선 수
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        s, e = map(int, input().split())

        adj_list[s].append(e)
        adj_list[e].append(s)

    # print(adj_list) # [[], [2], [1, 3], [2]]

    # DFS를 통해서 각 노드의 시작점마다 DFS실행한 다음에
    # max_length를 각 노드의 시작마다 계속해서 구하고
    # 마지막에 백트래킹해서 visited했던걸 다시 초기화해주면 끝날듯?

    ans = 0 # 전체 케이스에서의 최장 경로 저장용

    # 모든 정점을 시작점으로 DFS적용
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True # 시작점 방문체크
        DFS(i, 1)  # 길이 1부터 시작
        visited[i] = False # 시작점 백트래킹

    print(f"#{tc} {ans}")