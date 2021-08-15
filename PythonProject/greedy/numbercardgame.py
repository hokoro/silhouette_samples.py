n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
answer_list = []

for i in range(n):
    answer_list.append(min(arr[i]))

print(max(answer_list))