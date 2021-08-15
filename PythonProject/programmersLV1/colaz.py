def solution(num):
    answer = 0
    count = 0

    while num!=1:
        if count == 500:
            return -1

        if num %2 ==0:
            num = num//2
            answer +=1
            count+=1
        else:
            num = num*3 +1
            answer+=1
            count +=1
    return answer


n= 6

print(solution(n))

n= 16

print(solution(n))

n= 626331
i = 0
j = 0
print(solution(n))



