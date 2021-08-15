#나머지 와 몫이 같은수 
'''
어떤수를 입력받고 나머지와 몫이 같은수 를 구하고 해당 되는 모든수의 합을 구하는 방식 
N = int(input())
sum = 0 모든 수의 합을 구할 변수 
N = 1 나머지와 몫이 같은수는 0 
N = 2 나머지와 몫이 같은수는 3 
N = 3 나머지와 몫이 같은수는 4 8 
N = 4 나머지와 몫이 같은수는 5 10 15 
N = 5 나머지와 몫이 같은수는 6 12 18 24
'''
N = int(input())
#효율 1등 가우스 덧셈법 = 시그마 등차수열 덧셈법 

sum_1 = int((N-1) *N *(N+1)/2)  
print(sum_1)
#효율을 최대한 끌어올린 코드 
a = [i for i in range(N+1,N**2,N+1) if i %N == i//N]
print(sum(a))
#효율 있는 한줄 짜리 코드 = 리스트 

a = [i for i in range(1,N**2) if i%N == i//N]
print(sum(a))

#내가 제일 먼저 생각한 코드 
b = []

for i in range(1,N**2):
    if i %N == i//N:
        b.append(i)

print(sum(b))