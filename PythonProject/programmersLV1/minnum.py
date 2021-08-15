def solution(arr):
    answer = []
    answer = arr

    answer.remove(min(answer))
    if not answer:
        return [-1]


    return answer
arr= [1,2,3,4]
print(solution(arr))

arr= [10]
print(solution(arr))
