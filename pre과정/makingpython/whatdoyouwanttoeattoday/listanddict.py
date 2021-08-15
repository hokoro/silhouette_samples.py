information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}
foods = ["된장찌개","피자","제육볶음"]

print(information.get("취미"))

#dict 값 추가해보기
information["특기"] = "피아노"
information["사는곳"] = "서울"
del information["좋아하는 음식"]
print(information)
print(len(information)) #information 에 들어가있는 정보 의 길이를 측정

#dict 초기화
information.clear()
print(information)

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[-1])
print(foods[-2])
print(foods[-3])

foods.append("김밥")
#del foods[1]
foods.remove("피자")

print(foods)