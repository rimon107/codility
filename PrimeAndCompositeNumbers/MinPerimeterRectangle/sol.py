from sys import maxsize

def solution(N):
    i = 1
    result = maxsize
    d = N
    factors = []
    while i*i < N:
        if N%i == 0:
            d = N//i
            factors.append((i,d))
        i += 1
    if i*i ==N:
        factors.append((i,i))
    for item in factors:
        result = min(result, (item[0]+item[1]))
    return result * 2


if __name__=="__main__":
    A = [1, 30, 15486451, 982451653]
    for a in A:
        res = solution(a)
        print(res)