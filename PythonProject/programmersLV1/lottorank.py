def solution(lottos, win_nums):
    answer = []
    zero_count = lottos.count(0)
    correct = []
    correct_num = []
    for i in lottos:
        if i in win_nums:
            correct.append(i)
    correct_num.append(len(correct)+zero_count)
    correct_num.append(len(correct))

    for i in correct_num:
        if i==6:
            answer.append(1)
        elif i==5:
            answer.append(2)
        elif i==4:
            answer.append(3)
        elif i==3:
            answer.append(4)
        elif i==2:
            answer.append(5)
        else:
            answer.append(6)


    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos,win_nums))
lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos,win_nums))

