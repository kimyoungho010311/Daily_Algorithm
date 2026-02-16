import sys, heapq
sys.stdin = open('input.txt')

'''
초기에 최대 힙이 비어있을 때 2가지 연산을 수행해야한다.
1. 자연수 X를 삽입
2. 최대 힙의 루트 노드의 키값을 출력하고, 해당 노드를 삭제 -> pop

큰 키값이 여러개일 경우 그 중 하나만 삭제된다.

- INPUT
    T: TestCase
    N: 각 테케별로 연산의 수 ( 1 <= N <= 100000 )
    N개의 줄에 걸쳐 연산 정보가 주어진다.
        연산1: 2개의 자연수 1 x가 주어지며 x를 최대 힙에 추가하는 연산을 해야한다.
        연산2: 자연수 2가 주어지며 최대 루트 키값을 출력 및 노드 삭제
- OUTPUT
    각 테케별 연산2 결과를 출력한다.
    
result 리스트에 각 연산 결과 추가한 다음에 한번에 출력하자
'''

T = int(input())
# T = 1

for tc in range(1, T+1):
    heap = []
    result = [] # 출력 결과 담는 배열

    N = int(input()) # 각 테케별 연산 횟수
    for _ in range(N):
        # 연산이 뭐가 올지 몰라서 리스트로 받음.. 뭔가 방법 있을거같음
        order = list(map(int, input().split()))

        if order[0] == 1:
            heapq.heappush(heap, -order[1])

        # 만약 맨 앞에 있는걸 출력하고싶으면 pop 하고 abs 씌우면 끝남?
        elif order[0] == 2:
            if heap: # heap이 비어있는게 아니면
                result.append(abs(heapq.heappop(heap)))
            else:
                result.append(-1)

    print(f"#{tc} ", end='')
    for elem in result:
        print(f"{elem}",end=' ')
    print()