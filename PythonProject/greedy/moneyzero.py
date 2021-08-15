N,K = map(int, input().split())
money_list = [int(input()) for _ in range(N)]
money_list.sort(reverse=True)
print(money_list)
i = 0
answer = 0
while K != 0:
    if K %money_list[i]>=0:
        answer = answer + K // money_list[i]
        K = K % money_list[i]
    i+=1


print(answer)


'''

def greedy(money,K):
    money = reversed(money)
    count = 0
    total = K
    for i in money:
        if i <= total and total % i >= 0:
            cnt = total //i
            count += cnt
            total -= i * cnt
        if total ==0:
            break
    return count

money = []
N,K = map(int,input().split())

for i in range(N):
    a = int(input())
    money.append(a)

print(greedy(money,K))

'''