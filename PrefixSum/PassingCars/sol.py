
def solution(A):
    l = len(A)
    d = [0] * l
    s = 0
    for i in range(l-1, -1, -1):
        if A[i]==1:
            s += 1
        if A[i]==0:
            d[i] = s
    res = sum(d)
    if res > 1000000000:
        return -1
    return res


if __name__=="__main__":
    A = [[0, 1, 0, 1, 1],]
    for a in A:
        res = solution(a)
        print(res)