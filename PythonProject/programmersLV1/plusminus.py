def solution(absolutes, signs):
    answer = 0
    pair = list(zip(absolutes, signs))
    for i in range(len(pair)):
        if pair[i][1] == True:
            answer += pair[i][0]

        else:
            answer += (-1 * pair[i][0])

    return answer