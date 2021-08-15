'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

test_case = int(input())
stack_ans = []
answer_list = []
command = ''
for i in range(test_case):
    command = input()
    if command == 'size':
        answer_list.append(len(stack_ans))
    elif command == 'empty':
        if stack_ans:
            answer_list.append(0)
        else:
            answer_list.append(1)
    elif command == 'pop':
        if not stack_ans:
            answer_list.append(-1)
        else:
            answer_list.append(stack_ans[-1])
            del stack_ans[-1]

    elif command == 'top':
        if not stack_ans:
            answer_list.append(-1)
        else:
            answer_list.append(stack_ans[-1])

    else:
        final_str = command.split()
        stack_ans.append(int(final_str[-1]))
for i in answer_list:
    print(i,end = '\n')