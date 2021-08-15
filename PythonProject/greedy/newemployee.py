import numpy as np

T = int(input())
grade_list = []
for _ in range(T):
    N = int(input())
    for _ in range(N):
        (x,y) = list(map(int,input().split()))
        grade_list.append((x,y))
    answer_list = sorted(grade_list)
    print(answer_list)

