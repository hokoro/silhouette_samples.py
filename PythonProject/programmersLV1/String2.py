def solution(s):
    answer = True
    if s.isnumeric() == True and (len(s) == 4 or len(s) == 6) :
        answer = True
    else:
        answer = False

    return answer


s = "a234"
print(solution(s))
s = "1234"
print(solution(s))
