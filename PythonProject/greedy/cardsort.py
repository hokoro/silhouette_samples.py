test_case = int(input())
card_list = [int(input()) for _ in range(test_case)]
card_list.sort()
answer = 0
answer_list = []
for i in card_list:
    answer += i
    answer_list.append(answer)

if len(answer_list) == 1:
    print(sum(answer_list))
else:
    del answer_list[0]
    print(sum(answer_list))

