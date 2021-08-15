def solution(s):
    answer = True
    pcount = s.count('p') + s.count('P')
    ycount = s.count('y') + s.count('Y')
    if pcount == ycount:
        answer = True
    else:
        answer =False
    return answer

s = "pPoooyY"
print(solution(s))
s= "Pyy"
print(solution(s))