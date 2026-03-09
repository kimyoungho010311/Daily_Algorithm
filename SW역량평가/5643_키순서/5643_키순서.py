import sys
sys.stdin = open('input.txt')

T = int(input())
"""
핵심로직
Floyed-Wshall이다. 해당 알고리즘은 최단거리를 찾는게 목적인 알고리즘이다.
3중 반복문을 통하여 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 점화식을 실행한다.

하지만 해당 알고리즘은 최단거리를 찾는 것 뿐 아니라 '경유지'의 존재를 확인하는데도 사용이 가능하다.
"""
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    # dist배열을 선언해서 모두 False로 채우고 시작하며, 알고리즘을 돌려 경유지가 있으면 True로 바꾼다.
    dist = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        # 2. 입력받은 비교 결과 (a, b)에 대해 dist[a][b] = True 설정 (a < b 의미)
        a, b = map(int, input().split())
        dist[a][b] = True
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][k] and dist[k][j]:
                    # dist[i][j] = True (i < k 이고 k < j 이므로 i < j 임, 삼단논법)
                    dist[i][j] = True
    count = 0
    # 아래는 모든 dist를 돌아다니면서 i->j, j->i가 모두 True인 경우를 구한다.
    # 반드시 모두 True여야 한다. 그래야 자신의 위치(순서)를 정확히 알 수 있기 때문이다.
    for i in range(1, N+1):
        can_compare = 0
        for j in range(1, N+1):
            if i == j:
                continue
            if dist[i][j] or dist[j][i]:
                can_compare += 1
        if can_compare == N - 1: # 나를 제외한 사람(N-1)과 모두 비교 가능하면 내 순위를 알 수 있따.
            count += 1

    print(f"#{tc} {count}")