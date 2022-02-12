def timeout_solution(A):
    diff = None
    l = len(A)
    for i in range(l-1):
        i_diff = abs(sum(A[:i+1]) - sum(A[i+1:]))
        if diff is None:
            diff = i_diff
        if i_diff < diff:
            diff = i_diff 
    return diff

def solution(A):
    diff = None
    l = len(A)
    pre = [0] * (l)
    suff = [0] * (l)
    pre[0] = A[0]
    suff[l-1] = A[l-1]

    for i in range(1, l):
        pre[i] = pre[i-1] + A[i]

    for i in range(l-1, 0, -1):
        suff[i-1] = suff[i] + A[i-1]

    for i in range(l-1):
        i_diff = abs(pre[i] - suff[i+1])
        if diff is None:
            diff = i_diff
        if i_diff < diff:
            diff = i_diff 
    return diff

if __name__=="__main__":
    # A = [-1000, 1000]
    A = [1, 2, 3, 4, 2]
    # A = [3, 1, 1]
    res = solution(A)
    print(res)