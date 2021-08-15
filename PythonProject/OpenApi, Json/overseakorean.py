import requests
import json
url = " http://apis.data.go.kr/B260004/OverseasKorProvideService2/getKorProvideList2"

res = requests.get(url)
text= res.text #정보를 확인 하기 위해서는 인간이 확인 할수 있는 문자인 text 문자로 바꿔줘야 한다.
MD_json = json.loads(text)

print(json.dumps(MD_json,indent = 4 ,sort_keys=True))
'''
해당 내용에는 사이트 에서 알려주는 응답 구조를 보면 뭘 나타내는지 확실하게 알수가 있다.
'''

