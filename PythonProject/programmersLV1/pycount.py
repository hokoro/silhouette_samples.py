def solution(nums):
    answer = 0
    busket = []
    for i in range(len(nums)):
        if nums[i] not in busket:
            busket.append(nums[i])


    if int(len(nums)/2) < len(busket):
        answer = int(len(nums)/2)

    if int(len(nums)/2) == len(busket):
        answer  = len(busket)

    if int(len(nums)/2) > len(busket):
        answer = len(busket)

    return answer


nums = [3,1,2,3]
print(solution(nums))
nums = [3,3,3,2,2,4]
print(solution(nums))
nums = [3,3,3,2,2,2]
print(solution(nums))