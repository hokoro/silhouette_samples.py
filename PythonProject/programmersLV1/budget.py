from itertools import combinations
def solution(d, budget):
    answer = 0
    d.sort()
    while budget < sum(d):
        d.pop()
    answer = len(d)
    return answer



d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))


d = [2,2,3,3]
budget = 10
print(solution(d,budget))
