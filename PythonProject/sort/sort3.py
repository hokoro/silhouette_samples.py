import sys
N= int(input())

answer_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())

    answer_list[input_num] = answer_list[input_num] + 1

for i in range(10001):
    if answer_list[i] != 0:
        for j in range(answer_list[i]):
            print(i)
