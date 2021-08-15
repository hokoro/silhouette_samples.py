import heapq
import sys

N = int(input())
heap_list = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap_list,(-num,num))
    else:
        if heap_list:
            print(heapq.heappop(heap_list)[1])
        else:
            print(0)