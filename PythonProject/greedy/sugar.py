sugar = int(input())
num = 0
while sugar != 0:
    if sugar %5 ==0:
        num+= sugar//5
        break

    sugar -= 3
    num+=1
    if sugar <0:
        num = -1

        break


