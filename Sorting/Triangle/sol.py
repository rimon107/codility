
def solution(A):
    triangle = 0
    size = len(A)
    flag1 = False
    flag2 = False
    flag3 = False
    if size<3:
        triangle = 0
    else:
        A.sort()
        for i in range(size-1,1, -1):
            if A[i] + A[i-1] > A[i-2]:
                flag1 = True
            if A[i-1] + A[i-2] > A[i]:
                flag2 = True
            if A[i] + A[i-2] > A[i-1]:
                flag3 = True
            if flag1 and flag2 and flag3:
                triangle = 1
                break
    return triangle


if __name__=="__main__":
    A = [[10, 2, 5, 1, 8, 20],[20, 1, 1]]
    for a in A:
        res = solution(a)
        print(res)