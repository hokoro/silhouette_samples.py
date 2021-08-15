N = int(input())
lofe = []
for i in range(N):
    L = int(input())
    lofe.append(L)

lofe.sort(reverse=True)

for i in range(len(lofe)):
    lofe[i] = (i+1)*lofe[i]


print(max(lofe))
