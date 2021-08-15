def solution(n):
    answer = 0
    busket = []

    for i in range(1,n+1):
        if n % i ==0:
            busket.append(i)

    print(busket)
    answer = sum(busket)
    return answer

n = int(input())
print(solution(n))