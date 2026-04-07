# import sys
# sys.stdin = open('input.txt')
#
# """
# 대회 우승하면 보너스 상금 흭들할 기회를 부여받는다.
# 우승자는 숫자판들 중에 두 개를 선택해서 정해진 횟수만큼 서로의 자리를 교환할 수 있다.
#
# 다 교환하면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
# 오른쪽 끝부터 1원이고 왼쪽으로 갈 수록 10씩 커진다.
#
# 반드시 횟수만큼 교환이 이루어져야하고 동일한 위치의 교환이 중복되어도 된다.
#
# """
#
# T = int(input())
# '''
# 모든 자리가 바뀐 전적이 있으면 맨 뒷자리끼리만 바꾸자
#
# 그리고 만약 맨 뒷자리 두개가 같으면 그냥 남은 반복 휫수 무시하고 출력해버리기~
#
# 각 반복마다 배열에서 max min 찾고 만약 index(max) > index(min) 면 min이 더 앞에 있는거라서 max로 옮겨준다.
#
# 그리고 반약 반복횟수가 배열의 길이만큼 도달하면(이미 정렬이 완성된다면) 이제 맨 뒤에 두자리만 바꾸면서 모든 교환횟수를 마무리한다.
#
# 만약 반복 횟수가 배열의 길보다 작다면 아직 정렬된게 아니라 배열을 순회하면서 정렬한다
# 이래야 중복 정렬이 안될듯?
#
# 아니다... 걍 정렬 떄린다음에 남은 교환횟수(총 교환 - 배열 길이 // 2) 하면 될려나?
# '''
# for tc in range(1, T + 1):
#     # 숫자 자리판, 교환 횟수
#     N, M = map(str, input().split())
#
#     M = int(M)
#     numbers = []
#     for n in N:
#         numbers.append(int(n)) # [1, 2, 3]
#
#     if M > 1: # 교환횟수가 1 이상인 경우에만 이렇게 수행한다.
#         numbers.sort(reverse=True)
#         remain_swap_count = M // len(numbers)
#
#         for _ in range(remain_swap_count):
#             tmp = 0
#
#             tmp = numbers[-1]
#             numbers[-1] = numbers[-2]
#             numbers[-2] = tmp
#
#     elif M == 1: #만약에 1보다 작은 경우에는 아래 로직을 수행한다.
#         # min, max값을 찾을때 min은 앞에서부터 max는 뒤에서부터 찾아야한다.
#         # 그러니깐 일단 numbers 에서 min, max 를 찾은 다음에 각각 앞 뒤에서 순회를 하면서
#         # 해당 값을 찾았을 때 인덱스를 구해서 서로 바꿔줘야하나..?
#
#         max_num, min_num = max(numbers), min(numbers)
#         # 먼저 max 값 찾기 위해서 뒤에서부터 순회한다.
#         for idx in range(len(numbers)-1, -1, -1):
#             if numbers[idx] == max_num:
#                 max_idx = idx
#
#         for idx in range(len(numbers)):
#             if numbers[idx] == min_num:
#                 min_idx = idx
#         # 이제 min, max의 인덱스 값을 다 찾았다. 그러면... 스왑해줘야겠지>?
#         tmp = max_num
#         numbers[max_idx] = min_num
#         numbers[min_idx] = tmp
#
#     result = "".join(map(str, numbers))
#
#     print(f"#{tc} {result}")



import sys
sys.stdin = open('input.txt')

# ㅆㅂ 이게 어떻게 DFS야

def dfs(count):
    global max_result
    # 현재 상태를 합쳐서 숫자로 만듬
    current_num = int(''.join(map(str, numbers)))

    # 이미 이 횟수에 이 숫자를 본 적이 있다면 리턴(가지치기)
    if (count, current_num) in visited:
        return
    visited.add((count, current_num))

    # 목표 횟수 도달하면 최댓값 갱신 후 리턴
    if count == M:
        max_result = max(max_result, current_num)
        return

    # 모든 가능한 두 자리 교환
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i] # 교환
            dfs(count + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i] # 복구(백트래킹)

T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    M = int(M)
    numbers = list(N)

    max_result = 0
    visited = set()
    dfs(0)

    print(f"#{tc} {max_result}")































































