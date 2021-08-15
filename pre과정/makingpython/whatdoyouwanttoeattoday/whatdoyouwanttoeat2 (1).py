import random 
#추가 , 삭제, 랜덤선택

lunch = ["된장찌개","피자","제육볶음","자장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if item == 'q':
        break
    else:
        lunch.append(item)

print(lunch)