def solution(s):
    return (''.join(reversed(sorted(s))))



s = "Zbcdefg"
#결과 "gfedcbZ"
print(solution(s))