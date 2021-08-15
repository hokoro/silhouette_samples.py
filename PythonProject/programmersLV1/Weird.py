def solution(s):
    answer = ''
    s = s.split(' ')

    for i in range(len(s)):
        for j in range(0,len(s[i])):
            if j %2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()
        answer += ' '

    return answer[:-1]


s = "try hello world"
print(solution(s))