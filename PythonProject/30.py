'''
from itertools import permutations
N = input()
N = list(N)
max_result = 0
result = list(permutations(N,len(N)))


for i in range(len(result)):
    if int('',join(result[i])) %30 !=0:
        print
    if int(''.join(result[i])) % 30 == 0 and max_result < int(''.join(result[i])):
        max_result = int(''.join(result[i]))



print(max_result)
'''
N = input() 
N = list(N) 
answer = -1 
max_num = sorted(N, reverse=True) 
max_num = int(''.join(max_num)) 
if max_num % 30 == 0: 
    answer = max_num 



print(answer)




