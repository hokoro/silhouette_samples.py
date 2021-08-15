fibonachi = [0,1]
N = int(input())

for i in range(2,N+1,1):
    fibonachi.append(fibonachi[i-1] + fibonachi[i -2])

print(fibonachi.pop())