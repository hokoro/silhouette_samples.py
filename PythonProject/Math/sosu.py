import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True



test_case = int(input())
sosu_list = list(map(int,input().split()))
sosucount = 0
for i in sosu_list:
    if is_prime_number(i) == True:
        print(is_prime_number(i))
        print(i,"는 소수이다 ")
        sosucount+=1
    else:
        continue

print(sosucount)


