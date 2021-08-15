def solution(new_id):
    answer = ''
    answer = new_id.lower()
    index = 0
    print(answer)
    for i in answer:
        if (i.islower() == False)or(i!='-') or(i!='_')or(i!='.'):
            answer = answer.replace(i,"")


    print(answer)
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
new_id = "z-+.^."
#print(solution(new_id))
new_id = "=.="
#print(solution(new_id))
new_id = "123_.def"
#print(solution(new_id))
new_id = "abcdefghijklmn.p"



