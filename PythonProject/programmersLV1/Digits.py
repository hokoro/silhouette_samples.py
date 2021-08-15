def solution(n):
    answer = 0
    count = 0
    num = n
    while(n>0): #자릿수 구하기
        count+=1
        n = int(n / 10)
        #print(n)

    for i in range(count):
        if count == 0:
            break
        else:
            answer = answer +(int(num/10**(count -1)))
            num = num % (10**(count-1))
            count -=1
    return answer

N = 123
print(solution(N))
N = 987
print(solution(N))
# 100 * 1 +10 * 2 + 1 * 3
