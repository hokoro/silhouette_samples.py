def solution(n):
    answer = 0
    busket = []
    for i in range(2,n+1): #판별할수
        for j in range(1,i):
            if i % j ==0:
                busket.append(i)

    if len(busket) == 2:
        answer = len(busket)

    print(answer)
    return answer
n=10
print(solution(n))

n = 5
print(solution(n))
