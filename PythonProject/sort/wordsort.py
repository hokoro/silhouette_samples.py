N = int(input())

answer_list = [input() for _ in range(N)]
my_set = set(answer_list)
answer_list = list(my_set)
answer_list.sort()  # 사전순 정렬
answer_list.sort(key=lambda x: len(x))

for i in answer_list:
    print(i, end='\n')
