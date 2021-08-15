N = int(input())
answer_list = []

for _ in range(N):
    (x,y) = list(map(int,input().split()))
    answer_list.append((x,y))

answer_list = sorted(answer_list)


for i in answer_list:
    print(i[0],i[1])