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

    
