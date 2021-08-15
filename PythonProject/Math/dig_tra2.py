import sys

N,B = map(int,input().split())
answer_list = []

def Dig_tra2(N,B,answer_list):
    if N % B >=10:
        answer_list.append(chr(N % B +55))
    else:
        answer_list.append(N%B)

    if N // B ==1:
        answer_list.append(N//B)
        return answer_list
    return Dig_tra2(N//B,B,answer_list)





