rest = []
n = 45
answer = 0
index = 0
while n>=1:
    rest.append(int(n%3))
    n = n/3
    index = index + 1

print(rest)
for i in rest:
    index =index -1
    answer = answer + i *(3**index)

print(answer)

rest = []
n = 125
answer = 0
index = 0
while n>=1:
    rest.append(int(n%3))
    n = n/3
    index = index + 1

print(rest)
for i in rest:
    index =index -1
    answer = answer + i *(3**index)

print(answer)

