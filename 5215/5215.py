import sys
sys.stdin = open('input.txt')

from itertools import combinations
"""
제한 칼로리를 넘기지 않으며, 민기가 젤 높은 만족도를 얻을 수 있는 조합을 생각해보자.
순열인가..? combination 사용하면 끝날거같은데

- INPUT
    T: TestCase
    N, L: 재료의 수, 제한 칼로리
    
    N개의 줄만큼 재료에 대한 점수와 칼로리: T K
- OUTPUT
    각 테케별로 가장 높은 조합의 만족도를 출력한다.

아마 백트레킹 필요할 듯
"""

T = int(input())

for tc in range(1, T+1):
    # 재료의 수, 제한 칼로리
    N, L = map(int, input().split())
    ingredients_info = {}
    max_happy = 0 # 최대 만족도를 담는 변수

    for _ in range(N): # N번만큼 반복해서 입력
        # 점수, 칼로리
        T, K = map(int, input().split())
        ingredients_info[T] = K

    keys = ingredients_info.keys()
    combi = []

    for k in range(1, len(keys)+1):
        combi.append(list(combinations(keys, k)))

    # 백트랙킹을 할 때 큰 수부터 더하면 빨리 끝날거같아서 반전
    combi.reverse()
    for row in combi:
        for elem in row:
            current_kal = 0
            current_happy = 0
            tmp = sorted(elem, reverse=True)
            # [500, 400, 300, 250, 100]
            # 정렬하면 위에처럼 나옴
            # 만족도의 최댓값을 구해야하기 때문에 정렬한 다음
            # 하나씩 더해보면서 만약 제한 칼로리 넘기면 백트래킹하는 방식으로 하면
            # 제한시간은 안넘을듯 ?
            # sorted 하는 방법 자체가 오래 걸리는게 아니라니깐... 잘 모르게씅ㅁ
            for idx in range(len(tmp)):
                current_kal += ingredients_info[tmp[idx]] # 해당 만족도 음식의 칼로리를 불러옴
                if current_kal > L:
                    break
                else:
                    current_happy += tmp[idx] # 해당 재료의 만족도를 현재 만족도에 추가함
                    max_happy = max(max_happy, current_happy)

    print(f"#{tc} {max_happy}")