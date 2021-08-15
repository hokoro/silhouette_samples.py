import re
T = int(input())
answer_list = []

for _ in range(T):
    count = 0
    N = int(input())
    reset = input()
    goal = input()
    if reset != goal:
        if reset.count('W') == reset.count('W') and reset.count('B') == reset.count('B'):
            count+=1
            answer_list.append(count)



print(answer_list)