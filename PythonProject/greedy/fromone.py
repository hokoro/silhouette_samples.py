# N 이 1 이 될떄까지 수행한다
N,K = map(int,input().split()) # map 메소드를 써서 한번에 입력 받는디.
count = 0
while N > 1:
    if N % K == 0: # 나누어 진다면 나누고
        N /=K
        count+=1

    else:       # 나눌수 없다면 1을 뺴주는 작업을 한다
        N -= 1
        count+=1


print(count)



#두번째 방법 O(logK)

N,K = map(int,input().split())

result = 0

while True:
    target = (N//K) * K #N이 K 로 나누어 떨어지는 수가 될떄까지 빼기
    result += (N-target) #1을 몇번 뺴야되는지 알수있음
    N = target

    if N<K:
        break

    result+=1
    N//=K


result +=(N-1)
print(result)