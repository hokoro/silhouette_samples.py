'''
딕셔너리에서 앞부분을 key 뒷부분을 value 라고 합니다. 
question = [
            {"질문": "취미는 무엇입니까","답변":"영화 보기입니다."},
            {"질문":"특기는 무엇입니까","답변":"댄스입니다"}
           ]

print(question)

question = {"취미는 무엇입니다":"영화 보기 입니다","특기는 무엇입니까":"댄스입니다."}
print(question)
'''

total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == 'q':
        break
    else:
        total_dictionary[question] = "" #질문만 등록했으니 답변은 당연히 없어야함


for i in total_dictionary: #i는 key 값
    print("해당하는 질문: ",i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)




