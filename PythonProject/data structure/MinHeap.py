import heapq
import sys

N = int(input())
heap_list = []
tt = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap_list, num)
        heapq.heappush(tt, num)
    else:
        try:
            print(heapq.heappop(heap_list))
        except IndexError:
            print(0)
'''
import sys
import heapq
test_case = sys.stdin.readline()
answer_list = []
heap_list = []

for i in range(test_case):
    heapnumber = sys.stdin.readline()
    if heapnumber == 0:
        if not heap_list:
            heapq.heappush(answer_list,0)
        else:
            heapq.heappush(answer_list,heapq.heappop(heap_list))
    else:
        heapq.heappush(heap_list,heapnumber)
for i in answer_list:
    print(i,end = '\n')
'''
'''
import sys
test_case  = sys.stdin.readline()
answer_list = []
heap_list = []
for i in range(test_case):
    heapnumber = int(sys.stdin.readline())
    if heapnumber == 0:
        if not heap_list:
            answer_list.append(0)
        else:
            answer_list.append(min(heap_list))
            heap_list.remove(min(heap_list))
    else:
        heap_list.append(heapnumber)


for i in answer_list:
    print(i,end = '\n')
'''


