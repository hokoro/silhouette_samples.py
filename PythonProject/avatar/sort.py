test_case = int(input())
answer_list = [int(input()) for _ in range(test_case)]
answer_list.sort()
for i in answer_list:
    print(i,end='\n')

