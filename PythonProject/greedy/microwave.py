Time = int(input())
A = 0
B = 0
C = 0
answer = 0
while True:
    if Time % 300 ==0:
         A = A + Time // 300
         Time = Time % 300


    if Time % 60 == 0:
        B = B + Time //60
        Time = Time % 60

    if Time <=0:
        answer = -1
        break

    Time = Time - 10
    C+=1



if Time <0:
    print(answer)
else:
    print(A,B,C)


'''
T = int(input())
if T % 10 != 0:
    print(-1)

else:
    A=B=C=0
    A = T//300
    B = (T%300)//60
    C = (T%300)%60//10
    print(A,B,C)
'''