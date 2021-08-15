def solution(A, B):

    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


arr1 = [[1, 4],
        [3, 2],
        [4, 1]]

arr2 = [[3, 3],
        [3, 3]]

print(solution(arr1,arr2))