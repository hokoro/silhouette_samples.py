weight = int(input())
answer = 0

while True:    
    if(weight%5) == 0:
        answer += weight//5
        break
    weight = weight -3
    answer += 1
    if weight <0:
        answer = -1
        break




print(answer)