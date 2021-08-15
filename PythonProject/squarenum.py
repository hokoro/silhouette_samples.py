
i = 1
check = 1

while(check!=0):
    num = int(input("자연수를 입력하시오"))
    for i in range(num + 1):
        if num ==(i * i) :
            print(i,"와",-1*i,"는",num,"의 제곱근이다") 
            i = 0
            num = 0
            break
        if num != (i * i)  :
            print("루트",num, "과 루트",-1*num,"는",num,"의 제곱근이다")
            #print(num ** 0.5, "와",-1*(num**0.5),"는",num,"의 제곱근이다")
            i = 0
            num = 0
            break