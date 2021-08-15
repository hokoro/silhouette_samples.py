
N,B = input().split()
N = list(N)
def Dig_tra(idx,N,B):
    if B>10:
        if ord("A") <= ord(N[idx]) and ord(N[idx]) <= ord("Z"):
            N[idx] = ord(N[idx]) % ord("A") + 10
            N[idx] = int(N[idx]) * (B ** (len(N) - (idx + 1)))
        else:
            N[idx] = int(N[idx]) * (B ** (len(N) - (idx+1)))

    else:
        N[idx] = int(N[idx]) * (B ** (len(N) - (idx + 1)))

    if idx+1 == len(N):
        return N
    return Dig_tra(idx+1,N,B)


result = Dig_tra(0,N,int(B))
print(sum(result))