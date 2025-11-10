def solution(ingredient):
    answer = 0
    target = [1,2,3,1]    
    
    for i in range(len(ingredient)-3):
        if ingredient[i] == 1:
            if ingredient[i+1] == 2:
                if ingredient[i+2] == 3:
                    if ingredient[i+3] == 1:
                        answer = answer + 1
    print(answer)
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
solution(ingredient)
