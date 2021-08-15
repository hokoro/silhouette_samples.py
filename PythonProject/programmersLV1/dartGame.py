def solution(dartResult):
    answer = 0
    bonus = ''
    lastoption = ''
    nowoption = ''
    nowpoint = 0
    lastpoint = 0
    dartResult_list = []
'''
    for i in dartResult:
        if i.isdigit() == True:
            nowpoint = int(i)
        if i.isalpha() ==True:
            bonus = i
        if i =='*' or i == '#':
            nowoption = i
            if nowoption == '*' and lastoption == '':
                #if bonus == 'S':

                #if bonus == 'D':

                #if bonus == 'T':
            if nowoption == '#' and lastoption == '':
                print('y')
            if nowoption == '*' and lastoption == '*':
                print('z')
            if nowoption == '#' and lastoption == '#':
                print('k')
            if nowoption == '#' and lastoption == '*':
                print('q')
            if nowoption == '*' and lastoption == '#':
                print('s')

        lastoption = nowoption
        lastpoint = nowpoint

    return answer
'''

dartresult = '1S2D*3T'
print(solution(dartresult))

dartresult = '1D2S#10S'
print(solution(dartresult))
dartresult = '1D2S0T'
print(solution(dartresult))
dartresult = '1S*2T*3S'
print(solution(dartresult))
dartresult = '1D#2S*3S'
print(solution(dartresult))
dartresult = '1T2D3D#'
print(solution(dartresult))
dartresult = '1D2S3T*'
print(solution(dartresult))
