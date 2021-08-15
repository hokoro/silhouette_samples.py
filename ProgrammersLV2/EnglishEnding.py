def solution(n, words):
    answer = []
    check_word = []
    person_count = 1
    word_count = 0
    last_word = ''
    for i in words:
        if len(i) == 1:
            answer.append(person_count)
            answer.append(word_count)
            break
        if i in check_word:
            answer.append(person_count)
            answer.append(word_count)
            break
        if person_count > n:
            person_count = 1
        if person_count == 1:
            word_count+=1
        if not check_word :
            check_word.append(i)
        elif last_word[-1] != i[0]:
            answer.append(person_count)
            answer.append(word_count)
            break
        person_count+=1
        last_word = i

    if not answer:
        answer.append(0)
        answer.append(0)
    return answer


n = 3
word = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,word))
n = 5
word = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n,word))
n = 2
word = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,word))

'''
def solution(n, words):
    before_words = []
    count = 0
    answer = [0, 0]
    for idx, word in enumerate(words):
        count %= n
        if idx >= 1: 
            if (word in before_words) | (before_words[-1][-1] != word[0]): 
                answer = [count + 1, 1 + idx//n]
                break
        count += 1
        before_words.append(word)
    return answer

'''