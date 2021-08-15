answer_list = [-1 for _ in range(26)]
str1 = input()
for i in range(len(str1)):
    answer_list[ord(str1[i]) - 97]=str1.index(str1[i])

for i in answer_list:
    print(i,end = ' ')