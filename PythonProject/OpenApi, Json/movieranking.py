#openAPI

'''
인터넷으로 얻어온 데이터를 우리가 가져올수 있도록 만든 도구
key 라는것이 필요한데 api 를 사용하면서 너무 많이 사용하거나 한사람이 독자적으로 많이 사용할
경우가 발생할수 있기 때문에 그것을 방지 하기 위해서 key 라는 것을 받아와서 쓴다.

'''

#영화 진흥 위원회 키값 : 469b8a6746565ce42eb6bb9f98585620

'''
가장 핵심적인것은 자신의 맞는 데이터를 사용하는게 가장 중요하고 
두번 쨰로 파이썬으로 가져올 url 이 핵심이다 
'''

import requests
import json
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=469b8a6746565ce42eb6bb9f98585620&targetDt=20210418"

res = requests.get(url)
text= res.text #정보를 확인 하기 위해서는 인간이 확인 할수 있는 문자인 text 문자로 바꿔줘야 한다.
MD_json = json.loads(text)

print(json.dumps(MD_json,indent = 4 ,sort_keys=True))
'''
해당 내용에는 사이트 에서 알려주는 응답 구조를 보면 뭘 나타내는지 확실하게 알수가 있다.
'''

print(MD_json.keys()) #우리가 데이터를 사용하기 전에 key 가 뭘 나타내는지 확인 해야 한다
#dict_keys(['boxOfficeResult']) 저장된 데이터 가 뭘 나타내는지 확인
print(MD_json['boxOfficeResult'].keys())
#boxofficeresult 에는 boxofficetype | dailyboxofficeList | showrange 이렇게 3가지로 출력된다

#모든 데이터를 출력 시키기 위해서 반복문을 사용해서 출력해보자

for i in MD_json['boxOfficeResult']['dailyBoxOfficeList']:
    print(i['rank'],i['rankOldAndNew'],i['movieCd'],i['movieNm'],i['salesAmt'])
    #i 만 하면 해당 영화의 모든 정보가 다 가져와 진다 따라서 배열 사용!! 해서 필요한 정보를 응답 필드를 적어서만출력


#pandas 방식으로 사용

import pandas as pd
movie = []
for i in MD_json['boxOfficeResult']['dailyBoxOfficeList']:
    movie.append([i['rank'],i['rankOldAndNew'],i['movieCd'],i['movieNm'],i['salesAmt']])
data = pd.DataFrame(movie)

print(data)

'''    0    1         2                  3          4
0   1  OLD  20183003                 서복  555224070
1   2  OLD  20216710     명탐정 코난: 비색의 탄환  224087740
2   3  OLD  20200703  극장판 귀멸의 칼날: 무한열차편  130129020
3   4  OLD  20216492                노바디   88223700
4   5  OLD  20197434               자산어보   76156120
5   6  OLD  20215850          고질라 VS. 콩   70293070
6   7  OLD  20205144                미나리   40254460
7   8  OLD  20199630           어른들은 몰라요   41882010
8   9  OLD  20215046              노매드랜드   32498400
9  10  OLD  20200065               더 파더   15036070

Process finished with exit code 0



'''