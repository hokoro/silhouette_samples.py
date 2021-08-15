'''
def solution(n, lost, reserve):
    answer = 0
    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            answer = answer + 1
            reserve.remove(lost[i]-1)
            continue
        if lost[i] + 1 in reserve:
            answer = answer + 1
            reserve.remove(lost[i] + 1)
            continue
    n = n - len(lost)
    answer = answer + n
    return answer
'''
def solution(n, lost, reserve):
    reser_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    print(reser_del)
    print(lost_del)
    for i in reser_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i + 1 in lost_del:
            lost_del.remove(i+1)
    return n - len(lost_del)



n  = 5
lost = [2,4]
reserve = [1,3,5]

print(solution(n,lost,reserve))

n  = 5
lost = [2,4]
reserve = [3]

print(solution(n,lost,reserve))

n  = 3
lost = [3]
reserve = [1]

print(solution(n,lost,reserve))