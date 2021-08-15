test_case = int(input())
answer_list = []

for i in range(test_case):
    number = int(input())

    if number == 0 and len(answer_list)>0:
        del answer_list[-1]

    else:
        answer_list.append(number)


print(sum(answer_list))
