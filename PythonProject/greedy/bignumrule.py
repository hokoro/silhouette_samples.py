import time

start = time.time()

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

max1 = arr[n-1]
max2 = arr[n-2]
sum = 0
print(max1,max2)
count = k

for i in range(m):
    if count ==0:
       sum += max2
       count = k
    else:
        sum+= max1
        count-=1


print(sum)