import math
T = int(input())
answer= []

for i in range(T):

    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    xdistance = x2 - x1
    ydistance = y2 - y1

    distance = math.sqrt(pow(xdistance, 2) + pow(ydistance, 2))

    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        if r1 + r2 > distance and abs(r1 - r2) < distance:
            answer.append(2)
        elif r1 + r2 == distance or abs(r1 - r2) == distance:
            answer.append(1)
        else:
            answer.append(0)


t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    rs = r1 + r2
    rm = abs(r1 - r2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rs or d == rm:
            print(1)
        elif d < rs and d > rm:
            print(2)
        else:
            print(0)



for i in answer:
    print(i , end = '\n')

