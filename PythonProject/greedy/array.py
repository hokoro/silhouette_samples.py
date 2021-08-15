n,m = map(int,input().split())
arrA = [list(map(int,input().split())) for _ in range(n)]
arrB = [list(map(int,input().split())) for _ in range(n)]
count = 0

def changeall(start,arr):
    x,y = start
    for i in range(x,x+3):
        for j in range(y,y+3):
            arr[i][j] = 1 - arr[i][j]


for i in range(n-2):
    for j in range(m-2):
        if arrA[i][j] != arrB[i][j]:
            count+=1
            changeall((i,j),arrA)


flag = 0
for i in range(n):
    if arrA[i] != arrB[i]:
        print(-1)
        flag = 1
        break
if flag == 0:
    print(count)