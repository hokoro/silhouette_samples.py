def solution(arr):

    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
        else:
            if answer[-1] != arr[i]:
                answer.append(arr[i])
    return answer



arr	=[1,1,3,3,0,1,1]
print(solution(arr))
arr	=[4,4,4,3,3]
print(solution(arr))