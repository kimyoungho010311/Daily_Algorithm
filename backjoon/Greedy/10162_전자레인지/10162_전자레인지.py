import sys
sys.stdin = open('input.txt')
'''
3개의 버튼 A B C 가 달린 전자레인지가 있다.
각 버튼마다 일정한 시간이 지정되어 있어 누를 때마다 그 만큼의 시간이 더해진다.
각각 5분, 1분, 10초이다.

음식마다 조리해야하는 시간 T가 주어진다.
버튼을 누른 횟수를 최소화 해야한다.

분 -> 초로 해야할듯
A: 300
B: 60
C: 10
'''
import sys
input = sys.stdin.readline

btn_dic = {'A': 300, 'B': 60, 'C': 10}
result = []

T = int(input())

for key in btn_dic.keys():
    result.append((T // btn_dic[key]))
    T = T % btn_dic[key]

if T != 0:
    print('-1')
else:
    print(*result)