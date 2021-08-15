N = int(input())
yogat_list = []
spot = 0
for _ in range(N):
    yogat_list.append(int(input()))

yogat_list = sorted(yogat_list,reverse=True)
answer = 0
for i in range(N):
    if i % 3 != 2:
        answer+=yogat_list[i]

print(answer)