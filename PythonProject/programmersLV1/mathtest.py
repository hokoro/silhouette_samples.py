def solution(answers):
    one = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    onecount = 0
    two = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    twocount = 0
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    threecount = 0
    for i in range(len(answers)):
        if answers[i] == one[i]:
            onecount +=1
        if answers[i] == two[i]:
            twocount+=1
        if answers[i] == three[i]:
            threecount +=1

    print(max(onecount,twocount,threecount))

    answer = []
    return answer



answers = [1,2,3,4,5]
print(solution(answers))
answers = [1,3,2,4,2]
print(solution(answers))
