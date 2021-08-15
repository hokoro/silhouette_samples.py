import sys
N = int(input())
answer_list = [int(sys.stdin.readline()) for _ in range(N)]
answer_list.sort()
for i in answer_list:
    print(i, end = '\n')