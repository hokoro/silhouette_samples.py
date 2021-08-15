def solution(N, stages):
    answer = {}
    dem = len(stages)
    for stage in range(1,N+1):
        if dem != 0:
            count = stages.count(stage)
            answer[stage] = count / dem
            dem-=count
        else:
            answer[stage] = 0

    print(answer.keys())

    return sorted(answer,key=lambda x : answer[x],reverse=True)



N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N,stages))

N = 4
stages = [4,4,4,4,4]
print(solution(N,stages))