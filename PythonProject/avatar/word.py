alphabet_count = [0 for _ in range(26)]
str1 = input()
str1 = str1.upper()

for i in range(len(str1)):
    alphabet_count[ord(str1[i]) - 65] += 1

if alphabet_count.count(max(alphabet_count)) >1:
    print('?')
else:
    print(chr(alphabet_count.index(max(alphabet_count))+65))