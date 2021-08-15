def solution(board, moves):
    answer = []
    bucket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] >0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                continue
            if bucket[-1:] == bucket[-2:-1]:
                answer += bucket[-1:]
                bucket = bucket[:-2]
            break

    return len(answer)*2




board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1],
        ]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))
