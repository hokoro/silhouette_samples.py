def solution(n):
    answer = ''
    for i in range(n):
        if i %2 ==0:
            answer = answer + '수'
        else:
            answer = answer + '박'
    return answer


n = 3
print(solution(n))

n = 4
print(solution(n))

