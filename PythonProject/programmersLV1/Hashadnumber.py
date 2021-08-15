import math
def solution(x):
    answer = True
    a = int(math.log10(x))
    rest = []
    x_a = x
    for i in range(a+1):
        rest.append(x//10 **a)
        x= x % 10**a
        a-=1

    if x_a % sum(rest) != 0 :
        answer = False
    return answer

arr = 10

print(solution(arr))

arr = 12
print(solution(arr))

arr = 11
print(solution(arr))

arr = 13
print(solution(arr))