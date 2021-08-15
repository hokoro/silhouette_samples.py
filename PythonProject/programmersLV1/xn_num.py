def solution(x, n):
    answer = []
    count = x
    for i in range(n):
        print(x)
        answer.append(x)
        x = x + count
    print(answer)

    return answer

x = -4
n = 2


print(solution(x,n))