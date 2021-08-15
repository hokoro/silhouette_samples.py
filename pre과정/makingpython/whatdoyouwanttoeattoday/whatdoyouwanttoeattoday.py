#오늘 점심이나 저녁 메뉴를 골라주는 프로그램을 만들어준다.
'''
핵심 기능 추가 삭제 선택 
1.선택 
있는 메뉴 중에 랜덤으로 선택 한다 
2.추가 

3.삭제

4.결과 출력 
'''
import random
import time
#print(random.choice(["된장찌개","피자","제육볶음"])) #random library 에 choice 함수를 사용 


#반복문으로 사용해도 됩니다 or print() 문장 30 개 가 있어도 된다. 
#코딩 세상에서 DRY 방식을 사용하는게 좋다 Don't repeat yourself 반복을 많아지는것을 피해라 
'''
for _ in range(30):
    #print(random.choice(["된장찌개","제육볶음","피자","치킨","떡볶이","라면","감자튀김"]))
''' 


'''
for x in range(30): #써서 반복을 실행해도 상관이 없음 
    print(x+1,"번쨰 저녁메뉴: ",random.choice(["된장찌개","피자","제육볶음","치킨","떡볶이","라면","감자튀김"]) )
'''

'''
while True:
    print(random.choice(["된장찌개","피자","치킨","떡볶이","라면","감자튀김"]))
    break #반복문을 탈출하는 예약어...
    print(random.choice(["된장찌개","피자","치킨","떡볶이","라면","감자튀김"]))
    time.sleep(1) #시간 함수를 사용해서 한문장 실행 후 1초동안 쉬기
'''   

print(random.choice(["된장찌개","피자","제육볶음"]))
print(random.choice(["김밥","졸면","돈까스"]))


lunch = random.choice(["된장찌개","피자","제육볶음"])
dinner = random.choice(["김밥","쫄면","돈까스"])

lunch = "냉장고"
print("오늘의 점심:",lunch)
print("오늘의 저녁:",dinner)

