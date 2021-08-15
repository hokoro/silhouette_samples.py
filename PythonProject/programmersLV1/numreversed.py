def solution(n):
    answer = []
    answer2 = 0
    count = 0
    num = n
    while (n > 0):  # 자릿수 구하기
        count += 1
        n = int(n / 10)
        # print(n)
    count2 = count
    for i in range(count):
        if count == 0:
            break
        else:
            answer.append(int(num / 10 ** (count - 1)))
            num = num % (10 ** (count - 1))
            count -= 1
    answer.sort(reverse= True)
    for i in range(0,count2):
        count2 = count2 -1
        answer2 = answer2 + answer[i] * (10**(count2))

    return answer2

n = 118372
print(solution(n))