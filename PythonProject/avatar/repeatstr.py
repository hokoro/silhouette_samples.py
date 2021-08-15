T = int(input())
answer_list = []

for i in range(T):
    R,S = input().split()
    R = int(R)
    sum = ''
    for j in range(len(S)):
        sum+=S[j] * R

    answer_list.append(sum)


for i in answer_list:
    print(i,end = '\n')



