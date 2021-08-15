#집합을 알아보자 = set
'''
중복된 데이터를 막아주는 set
순서가 없다는 점이다.

1 합집합 연산
겹치는 원소는 하나로 통일 시켜준다
+집합 두개를 하나로 합쳐줌

2.차집합 연산
겹치는 원소를 뺴주는 역할

3.교집합 연산
겹치는 원소만 뽑아주는 연산
+집합은 안에있는 원소 순서를 보장해 주는 것이 아니다 .
'''

foods = ["된장찌개","피자","제육볶음","된장찌개"]
print(foods)
#합집합 연산
foods_set = set(foods) #집합을 사용하면 합집합 연산이 자동으로 실행된다 .
#foods_set = set(["된장찌개","피자","제육볶음"])
print(foods_set)
'''
list:['된장찌개', '피자', '제육볶음']
set:{'된장찌개', '피자', '제육볶음'}
'''

#합집합 연산
menuA = set(["된장찌개","피자","제육볶음"])
menuB = set(["된장찌개","떡국","김밥"])

menuC = menuA | menuB

print(menuC)

#교집합 연산(겹치는 원소만 출력 )

menuC = menuA&menuB

print(menuC)

#차집합 연산(겹치는 원소를 빼고 나머지 출력)
menuC = menuA - menuB

print(menuC)

