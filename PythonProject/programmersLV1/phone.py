def solution(phone_number):
    answer = ''
    count = len(phone_number)
    for i in phone_number:
        if count >4:
            answer = answer + '*'
            count -=1
        else:
            answer = answer + i
            count-=1
    return answer





phone_number = "01033334444"
print(len(phone_number))
print(solution(phone_number))

phone_number = "027778888"
print(len(phone_number))
print(solution(phone_number))