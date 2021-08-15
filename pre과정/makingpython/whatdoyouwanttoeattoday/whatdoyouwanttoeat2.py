import random
import time 
#추가 , 삭제, 랜덤선택

lunch = ["된장찌개","피자","제육볶음","자장면"]

#추가 연산
while True:
    print(lunch)
    item = input("삭제할 음식을 추가 해주세요 : ")
    if item == 'q':
        break
    else:
        lunch.append(item)


set_lunch = set(lunch)
#삭제 연산 (차집합 연산 , 삭제는 집합을 이용해서 구현해야 한다. , 리스트도 삭제 구현 충분히 가능 하다.(집합은 같은 원소는 걸러내는 교집합 연산이 있기 때문에 좋다.))
while True:
    print(set_lunch)
    item = input("음식을 삭제 해 주세요 : ")    
    if item == 'q':
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch,"중에서 선택합니다.")
#대기 연산 + 출력연산 
for i in range(5,0,-1):
    print(str(i))
    time.sleep(1)

print(random.choice(list(set_lunch))) #집합을 리스트 로 초기화 한다음 리스트중에 하나를 무작위로 뽑는 함수를 만든다  
