import re
S = input()


S= list(map(int,re.findall('\d',S)))

print(S)


sum = S[0]
for i in range(1,len(S)):
    num = S[i]
    if num<=1 or sum <=1:
        print("A조건 실행")
        sum = sum + num
    else:
        print("B조건 실행")
        sum= sum * num


print(sum)