def solution(numbers, hand):
    answer = ''
    lastL = 10
    lastR = 12

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lastL = n
        elif n in [3, 6, 9]:
            answer += 'R'
            lastR = n
        else:
            n = 11 if n == 0 else n

            absL = abs(n - lastL)
            absR = abs(n - lastR)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = n
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = n
                else:
                    answer += 'R'
                    lastR = n

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] #"LRLLLRLLRRL"
hands = "right"
print(solution(numbers,hands))

'''
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2] #"LRLLRRLLLRR"
hands = "left"
print(solution(numbers,hands))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] #"LLRLLRLLRL"
hands = "right"
print(solution(numbers,hands))
'''