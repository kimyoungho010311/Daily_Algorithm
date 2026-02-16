import sys

# 입력 전체를 읽고 공백으로 분리
# 주의: math 모듈은 사용되지 않으므로 제거 가능하지만, 여기서는 그대로 둡니다.
input = sys.stdin.read
data = input().split() 

# 1. N과 M 추출 (정수 변환)
N = int(data[0])
M = int(data[1])

package_prices = []
indivisual_prices = []
# data[2]부터 가격 정보가 시작되므로, 인덱스 2부터 M*2개의 데이터를 처리합니다.

for i in range(M):
  # 인덱스 수정 및 정수형으로 변환
  # i=0일 때 data[2]와 data[3]이 읽히도록 인덱스 조정
  package_price = int(data[2 * i + 2])  # 2, 4, 6...
  indivisual_price = int(data[2 * i + 3]) # 3, 5, 7...

  package_prices.append(package_price)
  indivisual_prices.append(indivisual_price)

# 2. 최소 가격 결정 (정수 리스트이므로 올바르게 작동)
P_min = min(package_prices)
I_min = min(indivisual_prices)

# 3. 세 가지 시나리오 비용 계산

# A. 모두 낱개로 사기
cost_A = N * I_min

# B. 모두 패키지로 사기 (N을 초과하더라도)
# (N/6의 올림) * P_min
cost_B = ((N + 5) // 6) * P_min

# C. 패키지 + 나머지 처리 중 저렴한 방법으로 사기
# N // 6 개의 패키지 구매는 확정
base_cost = (N // 6) * P_min
# 나머지 (N % 6) 줄을 사는 비용 vs 패키지 1개를 추가로 사는 비용 중 더 저렴한 것을 선택
remainder_cost = min((N % 6) * I_min, P_min)

cost_C = base_cost + remainder_cost

# 4. 세 가지 비용 중 최소값 출력
min_cost = min(cost_A, cost_B, cost_C)
print(min_cost)