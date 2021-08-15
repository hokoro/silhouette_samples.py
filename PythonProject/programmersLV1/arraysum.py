def solution(arr1, arr2):
    ans = [[0 for j in range(len(arr1[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            ans[i][j] = arr1[i][j] + arr2[i][j]
    return ans


arr1 = [[1,2],
        [2,3]]



arr2 = [[3,4],
        [5,6]]

ans = []
ans = [[0 for j in range(len(arr1[0]))] for i in range(len(arr1))]
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        ans[i][j] = arr1[i][j] + arr2[i][j]
print(ans)