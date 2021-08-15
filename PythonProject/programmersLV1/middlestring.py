def solution(s):
    middleindex = 0
    middleindexnext = 0
    answer = ''
    if len(s) %2 ==0:
        middleindex = int(len(s)/2) -1
        middleindexnext = middleindex +1
        answer = s[middleindex] + s[middleindexnext]
    else:
        middleindex = int(len(s)/2)
        answer = s[middleindex]
    #else:
    return answer

s = "abcde"
print(solution(s))
s = "qwer"
print(solution(s))