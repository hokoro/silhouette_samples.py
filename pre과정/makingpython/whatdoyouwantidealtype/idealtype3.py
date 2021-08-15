'''
딕셔너리에서 앞부분을 key 뒷부분을 value 라고 합니다.
question = [
            {"질문": "취미는 무엇입니까","답변":"영화 보기입니다."},
            {"질문":"특기는 무엇입니까","답변":"댄스입니다"}
           ]

print(question)

question = {"취미는 무엇입니다":"영화 보기 입니다","특기는 무엇입니까":"댄스입니다."}
print(question)
이 방식으로 하는 방법

'''

total_list = []

while True :
    question = input("질문을 입력해 주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question,"답변": ""})



for i in total_list:
    print("질문:"+i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer

print(total_list)


