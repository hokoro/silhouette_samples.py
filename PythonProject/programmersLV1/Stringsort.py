def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])



strings = ["sun", "bed", "car"]
n = 1
print(solution(strings,n))

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings,n))