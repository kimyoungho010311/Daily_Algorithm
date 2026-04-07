import sys
sys.stdin = open('input.txt')

'''
왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보되어야 조망권 확보라고 말한다.
빌딩에 대한 정보가 주어질때 조망권이 확보된 세대의 수를 반환해라


그래프가 주어지면 완탐을 시작한다.

해당 지점에 세대가 존재한다면 플래그 변수를 선언해서 is_good = True로 선언한다.
그 다음 좌 우로 2칸씩 찾아보다가 한칸이라도 없다면 is_good = False로 변경한 다음 더 이상 찾아보지 말고 바로 종료한다.

이런식으로 계속 조망권 확보된 세대 찾으면 카운팅 하면 끝

'''
T = 10

for tc in range(1, T + 1):
    # 건물의 개수
    N = int(input())
    buildings = list(map(int, input().split()))

    # 그래프로 주어지는게 아니라 건물 높이로 주어지는거네
    # 흠... 2칸씩 슬라이딩으로 탐색한다음에 해당 기준 건물이 가장 높으면

    # 아 그전에 가운데 값이 가장 큰 값과 같은지 비교하고 맞다면
    # 기준으로 좌우 + 2 칸만큼의 임시 리스트를 뽑아 낸 다음에
    # 가운에 값 제거 하고 max를 찾고 뺀 값을 최종 값에 더한다.

    # 아니면 다음칸으로 윈도를 넘긴다.

    result = 0
    for idx in range(2, len(buildings) - 2):
        tmp = buildings[idx - 2: idx + 3]
        max_building = max(tmp)
        mid_building = tmp[2]

        if max_building == mid_building:
            tmp.sort(reverse=True)
            result += max_building - tmp[1]

    print(f"#{tc} {result}")