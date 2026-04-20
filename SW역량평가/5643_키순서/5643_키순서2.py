import sys
sys.stdin = open('input.txt')
'''
1 ~ N번까지의 번호가 붙여져 있는 학생들이 있다. 이 중에서 두 명끼리만 키를 비교한다.
모든 학생의 키는 전부 다르다.
자신의 키가 몇번째인지 알 수 있는 학생의 수를 출력한다.

플로이드 워셜 알고리즘이다.
3중 반복문을 사용하여 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 점화식을 사용한다.

위 알고리즘은 최단거리뿐만 아니라, 경유지의 존재 유무도 알 수 있다.
'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    M = int(input())

    # 모두 False로 선언한 다음에 경유지가 있다면 True로 전환한다.
    dist = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        # 입력받은 비교 결과 (a b)에 대해 dist[a][b] = True로 설정 (a < b 의미)
        a, b = map(int, input().split())
        dist[a][b] = True

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][k] and dist[k][j]:
                    # 경유지가 존재한다면
                    dist[i][j] = True

    count = 0

    # 아래는 모든 dist를 돌아다니면서 경유지가 있는지 확인한다. 그래야 본인의 순서를 알 수 있다.
    for i in range(1, N+1):
        can_compare = 0
        for j in range(1, N+1):
            if i == j:
                continue
            # 만약 경유지가 존재한다면 비교가 가능할수도있다.
            if dist[i][j] or dist[j][i]:
                can_compare += 1
        # 마지막으로 can_compare할 수 있는 학생수가 본인을 제외한 숫자와 같다면
        # 모든 방향으로 이어져 있음으로 자신의 정확한 순서를 알 수 있다.
        if can_compare == N - 1:
            count += 1

    print(f"#{tc} {count}")