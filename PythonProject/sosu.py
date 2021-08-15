#소수와 합성수를 찾는 프로그램 을 만들어보자
#소인수 분해도 하는 프로그램 

answer = []

i= 1
rest = 0
check = 1  


while(check != 0):
    num  = int(input("판별할 수를 입력하세요 "))

    for i in range(num+1):
        try:
            if num % i == 0:
                rest = num/i
                answer.append(rest) 
        except ZeroDivisionError:
            continue
        else:
            continue
    answer.sort()
    print(answer)       
    
    if len(answer) >2:
        print("합성수 입니다 ")
    elif len(answer) == 2:
        print("소수 입니다 ")

    answer.clear()



