test_case = int(input())
answer_list =[]
for i in range(test_case):
    H,W,N = map(int,input().split())
    floors = N%H
    houess = (N//H) + 1
    if floors == 0:
        floors = H
        houess -= 1
    answer_list.append(100*floors+houess)


for i in answer_list:
    print(i,end = '\n')
