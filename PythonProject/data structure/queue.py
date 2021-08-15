test_case = int(input())
stack_list =[]
answer_list = []
command = ''

for i in range(test_case):
    command = input()
    if command == 'size':
        answer_list.append(len(stack_list))
    elif command == 'empty':
        if stack_list:
            answer_list.append(0)
        else:
            answer_list.append(1)

    elif command == 'front':
        if not stack_list:
            answer_list.append(-1)
        else:
            answer_list.append(stack_list[0])

    elif command == 'back':
        if not stack_list:
            answer_list.append(-1)
        else:
            answer_list.append(stack_list[-1])

    elif command == 'pop':
        if not stack_list:
            answer_list.append(-1)
        else:
            answer_list.append(stack_list[0])
            del stack_list[0]

    else:
        final_str = command.split()
        stack_list.append(int(final_str[-1]))


for i in answer_list:
    print(i,end = '\n')