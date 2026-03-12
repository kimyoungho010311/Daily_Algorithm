import sys, math
sys.stdin = open('input.txt')
'''
물은 가장 왼쪽에서부터 정수만큼 떨어진 거리만 물이 샌다
길이가 L인 테이프를 무한개 가지고 있다.

물을 막을 때 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안샌다.

물이 새는 곳의 위치와 테이프 길이 L이 주어질 때, 항승이가 필요한 테이프의 최소 개수를 구해라

테이프 자르기, 겹치기 불가능
'''

# 물 새는 곳 수, 테이프 길이
N, L = map(int, input().split())

pipe = list(map(int, input().split()))

# .. 음.. pipe 리스트를 모두 순회하는데 연속되는 자리가 있는걸 따로 모아서 해야할듯
# [[1, 2, 3], [5, 6], [8, 9, 10]] 이런식으로 만들고
# L로 최대한 자르면서 나머지? 몴?을 구해서 테이프 개수 구하면 끝날듯
pipe.sort()

count = 0
current_tape_end = 0 # 현재 테이프가 덮고있는 끝 지점

for p in pipe:
    # 현재 구멍이 테이프가 덮고 있는 범위를 벗어났다면
    if p + 0.5 > current_tape_end:
        count += 1
        # 새 테이프 붙임: (시작점 - 0.5) + L
        current_tape_end = (p - 0.5) + L
print(count)