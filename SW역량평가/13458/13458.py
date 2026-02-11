import sys
sys.stdin = open('input.txt')
"""
총 N개의 시험장, i번 시험장의 응시자 수는 Ai명이다.

감독관 -> 총감독관, 부감독관
총감동관은 한 시험장에서 감시 인원 B명
부감독관은 C명

각 시험장의 총감 1명은 필수, 부감은 여러 명 가능

각 시험장마다 있는 응시생 모두를 감시해야 한다. 이때 필요한 감독관 수의 최솟값을 출력

-INPUT
    N: 시험장 수
    Ai: 각 시험장 별 응시 인원 수
    B, C: 총감 감시 인원, 부감 감시 인원 (**총감은 한명만 있어야 한다**)
-OUTPUT
    최소 감독인원 수
"""
def sol1(cnt):
    """
    내가 푼거
    """
    for idx in range(len(Ai)):
        Ai[idx] -= B  # 각 반마다 총감을 배치해서 남은 감독인원만 Ai에 입력한다.
        cnt += 1  # 총감을 배치할 때마다 cnt += 1 해준다.
        tmp = Ai[idx] / C
        if tmp < 0:
            continue
        if not tmp.is_integer():
            cnt += int(tmp) + 1
        else:
            cnt += tmp
    return cnt

def sol2(cnt):
    '''
    잼미니가 푼거
    '''
    for num in Ai:
        # 총 감독관은 무조건 필요하다.
        cnt += 1
        remaining = num - B # 총 감독관 감시 인원 제외 인원

        if remaining > 0:
            # 올림 계산 공식: (A + B - 1) // B
            # 예: remaining이 1이고 C가 5일 때 -> (1 + 4) // 5 = 1 (부감독관 1명 필요)
            cnt += (remaining + C - 1) // C
    return cnt

N = int(input())  # 시험장 수
Ai = list(map(int, input().split()))  # 각 시험장 별 인원 수
Ai.sort()  # 정렬은 필요 없을거같긴 한데 기분이 좋아지니깐 추가.. [3, 4, 5]

B, C = map(int, input().split())  # 총감 수, 부감 수
cnt = 0  # 총 필요한 감독 수

cnt = sol1(cnt)

'''
몫을 어케 구하지
'''
print(int(cnt))