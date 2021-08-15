foods = ["된장찌개","피자","제육볶음"]

for x in range(30):
    print(x)

print(foods,end = '\n')
for i in range(len(foods)):
    print(foods[i],end = '\n')

for i in foods:
    print(i,end = '\n')

information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}

for x,y in information.items(): #key,value 값을 2가지 변수에 저장 하고 items 로 하나씩 가져오는 방식
    print(x)
    print(y)


