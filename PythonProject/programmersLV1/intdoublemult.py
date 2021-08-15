def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n/i == i:
            answer = int((n/i +1) **2)
            break
        else:
            answer = -1
    return  answer



n = 121
print(solution(n))
n = 1
print(solution(n))