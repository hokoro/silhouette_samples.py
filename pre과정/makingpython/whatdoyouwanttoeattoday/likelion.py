set_lunch = set(["된장찌개","피자","제육볶음","자장면"])
item = "자장면"

set_lunch = set_lunch - set([item])
'''
set_lunch 는 리스트 형태기 떄문에 집합으로 제거 할려면 
list 형태인 [] 상태에서 보내줘야 한다.
'''
print(set_lunch)