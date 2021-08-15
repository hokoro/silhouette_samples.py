#이항 계수
n,k = map(int,input().split())
answer = 0
n_k = n-k
n_sum = 1
k_sum = 1
n_ksum = 1

if k < 0 or k>n:
    print(0)
else:
    for i in range(1, n + 1):
        n_sum = n_sum * i

    for i in range(1, k + 1):
        k_sum = k_sum * i

    for i in range(1, n_k + 1):
        n_ksum = n_ksum * i
    print(int(n_sum /(k_sum * n_ksum)))

