import sys
sys.stdin = open('병합정렬.txt')


# 병합 정렬 함수
def merge_sort(arr):
    global count
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        count += 1

    return merge(left, right)


def merge(left, right):
    result = []
    l = r = 0
    len_l, len_r = len(left), len(right)

    while l < len_l and r < len_r:
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # 남은 부분 처리
    if l < len_l:
        result.extend(left[l:])
    if r < len_r:
        result.extend(right[r:])

    return result


# 입력 처리
T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    count = 0
    sorted_arr = merge_sort(arr)

    print(f"#{tc} {sorted_arr[N // 2]} {count}")