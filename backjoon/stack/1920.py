import sys
# 입력 속도 최적화를 위해 sys.stdin.readline 사용
input = sys.stdin.readline 

# 1. 배열 A 입력 및 Set 변환
# N (1 ≤ N ≤ 100,000)
N = int(input())

# A 배열을 Set으로 변환하여 저장
# Set은 탐색(in 연산) 시간이 평균 O(1)로 매우 빠릅니다.
A_set = set(map(int, input().split()))

# 2. M개 수 입력
# M (1 ≤ M ≤ 100,000)
M = int(input())

# M개의 수들을 리스트로 입력받음
M_list = list(map(int, input().split()))

# 3. M개의 수를 탐색하며 결과 출력
for target in M_list:
    # Set을 이용한 탐색
    if target in A_set:
        print(1)  # 존재하면 1 출력
    else:
        print(0)  # 존재하지 않으면 0 출력