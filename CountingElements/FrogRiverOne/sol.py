def timeout_solution(X, A):
    sec = -1
    if X in A:
        sec = A.index(X)
        for i in range(X-1, 0, -1):
            if i in A:
                ind = A.index(i)
                if ind > sec:
                    sec = ind
            else:
                return -1
    return sec

def solution(X, A):
    sec = None
    l = len(A)
    try:
        sec = A.index(X)
        s = set(A)
        d = 1
        for i in s:
            if d==X:
                break
            if i!=d:
                return -1
            d += 1
        ad = dict()
        sa = set()
        for i in range(l):
            if A[i] not in sa:
                sa.add(A[i])
                ad[A[i]] = i
        for _, value in ad.items():
            if value > sec:
                sec = value
    except ValueError:
        sec = -1
    return sec

if __name__=="__main__":
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    X = 5
    A = [2, 2, 2, 2, 2]
    X = 2
    res = solution(X, A)
    print(res)