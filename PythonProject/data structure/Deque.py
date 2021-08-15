test_case = int(input())
Deque_list = []
answer_list = []
command = ''

for i in range(test_case):
    command = input()

    if command == 'size':
        answer_list.append(len(Deque_list))

    elif command == 'empty':
        if Deque_list:
            answer_list.append(0)

        else:
            answer_list.append(1)

    elif command == 'front':
        if not Deque_list:
            answer_list.append(-1)
        else:
            answer_list.append(Deque_list[0])

    elif command == 'back':
        if not Deque_list:
            answer_list.append(-1)
        else:
            answer_list.append(Deque_list[-1])

    elif command == 'pop_front':
        if not Deque_list:
            answer_list.append(-1)
        else:
            answer_list.append(Deque_list[0])
            del Deque_list[0]

    elif command == 'pop_back':
        if not Deque_list:
            answer_list.append(-1)

        else:
            answer_list.append(Deque_list[-1])
            del Deque_list[-1]

    else:
        command_str = command.split()

        if command_str[0] == 'push_front':
            Deque_list.insert(0,int(command_str[1]))

        if command_str[0] == 'push_back':
            Deque_list.append(int(command_str[1]))

for i in answer_list:
    print(i,end = '\n')
