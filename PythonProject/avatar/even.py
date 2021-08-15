integerList = [int(input()) for _ in range(7)]
evenlist =[]


for i in integerList:
    if i % 2==0:
        continue
    else:
        evenlist.append(i)



if not evenlist:
    print(-1)

else:
    print(sum(evenlist))
    print(min(evenlist))
