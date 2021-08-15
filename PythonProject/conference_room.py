import sys
Count = int(input())

meeting = []

for i in range(Count):
    start,end = map(int,sys.stdin.readline().split())
    meeting.append((start,end))

print(meeting)