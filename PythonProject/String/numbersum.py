import re
test_case = int(input())

number = input()

numbers = re.findall("\d",number)

numbers = map(int,numbers)

print(sum(numbers))


