import random
food = random.choice(["된장찌개","피자","제육볶음"])

print(food)
if food == "제육볶음":
    print(food,"은 곱뺴기 주세요")
else:
    print(food,"그냥 주세요")
print("종료")