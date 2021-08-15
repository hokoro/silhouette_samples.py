'''
a = [i*j for j in range(2,10) for i in range(1,10)]
print(a)

# [(생성식) for j in range(범위) for i in range(범위)]
#처리 순서가 뒤에서 앞으로 이다 

a = [1.2,2.5,3.7,4.6]
for i in range(len(a)):  #a가 4 이기떄문에 
    a[i] = int(a[i])

print(a)


a = [1.2,2.5,3.7,4.6]
a = list(map(int,a))
print(a)

a= list(map(str,range(10)))
print(a)

a=(38,21,53,62,19,53)
print(a.index(53))
print(a.count(20))
for i in a:
    print(i ,end = ' ')

j = 0
while j<len(a):
    print(a[j],end = ' ')
    j = j+1


a = tuple(i for i in range(10) if i%2==0)
print(a)


a = (38,21,53,62,19)
print(min(a))
print(max(a))
print(sum(a))


a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i) ==5]
print(b)


a,b = map(int,input().split())

if a<1 and a>20:
    print("범위를 벗어났습니다")
if a<10 and a>30:
    print("범위를 벗어났습니다")

result = [2**i for i in range(a,b+1)]
result.pop(1)
result.pop(len(result)-2)
print(result)

import random

result = [ ]

for i in range(10):
    lotto_num = random.sample(range(1,51),7)
    lotto_num.sort()

    print(lotto_num)

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a)

a= [[10,20],
    [30,40],
    [50,60]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] ,end=' ') 
    print()
for i in range(len(a)):
    print(a[i])

for x,y in a:
    print(x,y)

i =0
while i < len(a):
    x,y =a[i]
    print(x,y)
    i+=1

a = [[1,2,3],[5,6,7],[8,9,10],[12,13,14]]

i = 0
while i < len(a):
    for j in range(len(a[i])):
        print(a[i][j],end = ' ')
    print()
    i= i +1

a = []  
 
for i in range(3):
    number = []              
    for j in range(2):
        number.append(0)     
    a.append(number)         
 
print(a)


a = [[0 for j in range(2)] for i in range(3)]
print(a)
a = [[0]*2 for i in range(3)]
print(a)

a = [[j*i for j in range(2)] for i in range(3)]
print(a)


a = [3,1,3,2,5]

result = []
for i in a:
    b = []
    for j in range(i):
        b.append(0)
    result.append(b)

print(result)

a = [[0]*i for i in [3,1,3,2,5]]
print(a)

import copy
a= [[10,20],[30,40]]
b = copy.deepcopy(a) #깊은 복사 (주소만 같은게 아니라) 데이터 까지 완전히 복사  
b[0][0] = 500
print(a)
print(b)

a= [[10,20],[30,40]]
b = a
b[0][0] = 500
print(a)
print(b)


a = [[[0 for i in range(3)] for j in range(4)]for k in range(2)]
print(a)
'''


