test_case = int(input())
guest = list(map(int,input().split()))
guest_sum = []

guest.sort()

for i in range(len(guest)):
    guest_sum.append(sum(guest[:i+1]))

print(sum(guest_sum))
