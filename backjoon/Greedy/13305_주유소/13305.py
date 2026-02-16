import sys
sys.stdin = open('input.txt')

"""
어... 가장 가격이 낮은 도시까지 최소한으로 주유한 다음에
가장 낮은 가격의 기름을 파는 도시에 도착하면 끝까지 갈만한 기름을 충전한다... 이게 맞나?
"""

N = int(input()) # 도시의 개수 (2 ≤ N ≤ 100,000)
distance = list(map(int, input().split()))
gas_prices = list(map(int, input().split()))

total_gas = 0 # 현재 남아있는 가스, 전체 사용한 가스(필요 없을 듯)

min_gas_price = min(gas_prices[:-1]) # 마지막 도시를 제외하고 가장 최저가의 기름을 파는 도시를 검색
print(min_gas_price)
# 거리:  2 3 1
# 도시: 5 2 4 1
for idx in range(N-1): # 도시의 개수만큼 반복 -> 마지막에 도달하면 도착지인걸로 간주함
    if gas_prices[idx] != min_gas_price:
        total_gas += gas_prices[idx] * distance[idx-1]
        distance.pop()
    else:
        print("최저가 도시에 도착!")
        tmp_gas = sum(list(map(lambda v: v * min_gas_price, distance)))

print(total_gas)
