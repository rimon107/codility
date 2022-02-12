
def solution(A):
    A.sort()
    res = A[-1] * A[-2] * A[-3]
    if A[-1] > 0 and A[-2] > 0 and A[-3] > 0:
        if A[0] < 0 and A[1] <0:
            a = A[0] * A[1]
            b = A[-2] * A[-3]
            if a > b:
                res = A[-1] * a
            else:
                res = A[-1] * b
    if A[0] < 0 and A[1] <0:
        if A[-1] > 0:
            a = A[0] * A[1]
            b = A[-2] * A[-3]
            if a > b:
                res = A[-1] * a
            else:
                res = A[-1] * b
    return res


if __name__=="__main__":
    A = [[-3, -2, -9, -7, -4, -1], [-5, 5, -5, 4], [-3, 1, 2, -2, 5, 6]]
    for a in A:
        res = solution(a)
        print(res)