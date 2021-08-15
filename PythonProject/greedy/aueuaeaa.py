N = int(input())
line = []
length_list = []

for _ in range(N):
    (start,end) = list(map(int,input().split()))
    line.append((start,end))

line.sort()
last_start = line[0][0]
last_end = line[0][1]
summer = 0
for i in line:
    if i[0] <=last_end and last_end<=i[1]:
        summer += (i[1] - last_start)
        last_start = i[0]
        last_end = i[1]

    else:
        #if summer ==0:

        length_list.append(summer)
        summer = 0
        last_start = i[0]
        last_end = i[1]

print(length_list)
print(sum(length_list))
