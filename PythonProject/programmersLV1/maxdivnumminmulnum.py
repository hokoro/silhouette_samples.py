def solution(n, m):
    answer = []
    sidemul = 1
    print(n,m)
    if n > m:

        for i in range(m,0,-1):

            if n%i == 0 and m%i == 0:
                n = n // i
                m = m // i

                sidemul = sidemul * i #최대공약수

            if i ==1:
                n = n // i
                m = m // i

                sidemul = sidemul * i  # 최대공약수
                answer.append(sidemul)
                answer.append(sidemul * n * m)
                print(answer)

    else:

        for i in range(n,0,-1):

            if n %i ==0 and m%i ==0:
                n = n // i
                m = m // i

                sidemul = sidemul *i

            if i == 1:
                n = n // i
                m = m // i

                sidemul = sidemul * i  # 최대공약수
                answer.append(sidemul)
                answer.append(sidemul*n*m)


    return answer




n=3
m = 12
print(solution(n,m))
n=2
m=5
print(solution(n,m))



