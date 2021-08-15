def solution(n):
    answer = []

    count = 0
    num = n
    while (n > 0):  # 자릿수 구하기
        count += 1
        n = int(n / 10)
        # print(n)

    for i in range(count):
        if count == 0:
            break
        else:
            answer.append(int(num / 10 ** (count - 1)))
            num = num % (10 ** (count - 1))
            count -= 1
    answer.reverse()
    return answer

n = 12345
print(solution(n))