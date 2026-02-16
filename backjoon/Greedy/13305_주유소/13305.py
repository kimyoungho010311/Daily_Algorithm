import sys
input = sys.stdin.readline

N = int(input())
# 거리와 주유소 가격 입력
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
total_cost = 0

# [핵심] 지금까지 지나온 주유소 중 가장 싼 가격을 저장할 변수
# 첫 번째 도시 가격으로 초기화
min_price = prices[0]

for i in range(N - 1):
    # 1. 현재 도시의 주유소 가격이 지금까지의 최저가보다 더 싸다면?
    # 사용자님이 생각한 "더 싼 곳을 찾으면 갈아탄다"는 로직의 실시간 구현입니다.
    if prices[i] < min_price:
        min_price = prices[i]

    # 2. "현재까지의 최저가"로 다음 도시까지의 거리만큼 결제
    # pop()을 쓰지 않고 인덱스 i를 사용하여 순차적으로 거리를 가져옵니다.
    total_cost += min_price * distances[i]

print(total_cost)