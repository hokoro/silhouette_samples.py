'''
text ,csv excel 데이터 뿐만 아니라
open api ,json 파일을 알아야 한다.

json =javascripts object notation
데이터를 효율적으로 저장하고 교환하는데 사용
이름 &값 의 집합  정렬된 리스트의 정보가 있음
python -> json
list       array
tuple
'''

#json 실습

import json

with open ('student_file.json') as json_file:
    json_data = json.load(json_file)
    print(json_data)

student_data = {
    "1.FristName": "youngsung", #이름 & 값 의 집합
    "2.LastName": "cheon",
    "3.Age": 25,
    "4.college": "chosun_university",
    "5.major": "computer_enginnering"
    #+ 정렬된 값으 리스트
}
#open 함수를 사용하여 json 파일을 open 한 다음에 as 를 사용하여 뒤에 별칭 이름으로 저장
#data 를 가져올때는 저장된 json_file 을 load() 메서드를 사용하여 불러와주면 된다.


#python 으로 바꾼 데이터를 다시 json 데이터를 바꾸고 싶을때 사용

st_json  = json.dumps(student_data,indent = 4,sort_keys=True) #생각보다 가독성이 떨어지는 문제가 있음
#indent = 숫자(데이터를 들여쓰기 쓰고 싶을때 사용하는 매개변수) , sort_keys = True (정렬조건 설정)
print(st_json)

