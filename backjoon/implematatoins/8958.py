test_case = int(input())

for _ in range(test_case):
    result = 0
    score = 0
    answer = input().strip()
    for ch in answer:
        if ch == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)