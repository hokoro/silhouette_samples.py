from itertools import combinations_with_replacement
def solution(nums):
    answer = 0
    numcheck = []
    count = 0
    for i in combinations_with_replacement(nums,3):
        if i[0] != i[1] !=i[2]:
            numcheck.append(i[0]+i[1]+i[2])
            count+=1

    for i in numcheck:
        for j in range(2,i):
            if i % j == 0:
                count-=1
                break



    answer = count
    return answer

nums = [1,2,3,4]
print(solution(nums))
nums = [1,2,7,6,4]
print(solution(nums))
