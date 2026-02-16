import sys
sys.stdin = open('input.txt')
# 입력을 위해 input 설정
N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
gas_prices = list(map(int, sys.stdin.readline().split()))

total_gas = 0

# 1. 마지막 도시를 제외하고 전체에서 가장 최저가인 기름값 찾기
# (사용자님의 기존 로직 유지)
min_gas_price = min(gas_prices[:-1])

# 2. distance를 뒤집어서 pop()이 효율적으로(뒤에서부터) 일어나도록 준비
# 파이썬의 pop()은 마지막 요소를 뺄 때 가장 빠르기 때문입니다.
distance.reverse()

for idx in range(N - 1):
    # 현재 도시의 기름값
    current_price = gas_prices[idx]

    # 지금 도시가 전체 최저가 주유소라면?
    if current_price == min_gas_price:
        # 남은 거리를 다 더해서 현재 최저가로 한꺼번에 계산
        # distance가 뒤집혀 있으므로 그대로 sum 하면 됩니다.
        total_gas += current_price * sum(distance)
        break  # 끝까지 다 채웠으므로 반복문 종료

    else:
        # 최저가 도시가 아니라면 다음 도시까지만 갈 만큼만 충전
        # distance.pop()은 뒤집힌 리스트의 마지막(즉, 원래의 앞부분)을 꺼냅니다.
        d = distance.pop()
        total_gas += current_price * d

print(total_gas)