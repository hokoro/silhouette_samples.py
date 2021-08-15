answer = []
for i in range(3):
    yoot = list(map(int,input().split()))
    if yoot.count(1) == 3 and yoot.count(0) == 1:
        answer.append('A')
    elif yoot.count(1) == 2 and yoot.count(0) == 2:
        answer.append('B')
    elif yoot.count(1) == 1 and yoot.count(0) == 3:
        answer.append('C')
    elif yoot.count(0) == 4:
        answer.append('D')
    else:
        answer.append('E')

for i in answer:
    print(i , end = '\n')