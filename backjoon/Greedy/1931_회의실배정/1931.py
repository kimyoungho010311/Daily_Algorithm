import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
한 개의 회의실이 있다.
이를 사용하고자 하는 N개의 회의에 대하여 사용표를 만들려고한다.
각 회의 I에 대해 시작, 끝 시간이 주어져 있고, 각 회의가 곂치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아본다.

중간에 중단 불가
끝나자마자 바로 시작함
시작과 끝이 동일하면 바로 끝난거임 -> 이것도 카운팅 ㄱㄱ
'''
# 회의 수
N = int(input())
meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append([s, e])
# [1, 4]
meetings.sort(key=lambda x: (x[1], x[0]))

start_meeting = meetings[0]
meetings = meetings[1:]
count = 1


for meeting in meetings:
    start, end = meeting

    if start_meeting[1] <= start:
        start_meeting = meeting
        count += 1

print(count)