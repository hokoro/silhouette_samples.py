def solution(array, commands):
    answer = []
    busket = []
    indexpoint = 0
    for i in range(len(commands)):
        busket = array[commands[i][0] -1:commands[i][1]]
        indexpoint = commands[i][2] -1
        busket.sort()
        answer.append(busket[indexpoint])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))