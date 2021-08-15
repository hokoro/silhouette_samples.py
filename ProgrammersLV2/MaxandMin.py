import re
def solution(s):
    max = ''
    min = ''
    answer = ''

    s = s.split('-')
    print(s)
    #numbers = list(map(int, numbers))
    #numbers.sort()
    #max = str(numbers[-1])
   #min = str(numbers[0])

    answer += min
    answer += max
    return answer


s = '52431'
print(solution(s))
s = '-5-2-4-3-1'
print(solution(s))