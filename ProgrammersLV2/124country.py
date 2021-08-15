def solution(n):
    menu = ['4', '1', '2']
    answer = ''
    while n:
        answer = menu[n % 3] + answer
        n = n // 3 - (n % 3 == 0)

    return answer


print(solution(10))