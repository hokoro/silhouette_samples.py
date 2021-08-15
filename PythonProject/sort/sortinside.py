import re
number = input()
answer = ''
number = re.findall("\d",number)


number = list(map(int,number))
number.sort(reverse=True)


for i in number:
    answer+=str(i)



print(answer)

