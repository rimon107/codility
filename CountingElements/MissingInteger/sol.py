def solution(A):
    l = len(A)
    if l==0:
        return 1
    
    bl = [False] * (l+2)
    res = 1
    s = set(A)
    SL = list(s)
    for element in SL:
        if element > 0 and element < (l+2):
            bl[element] = True
    for i in range(1, len(bl)):
        if not bl[i]:
            res = i
            break
    return res


if __name__=="__main__":
    A = [[1, 3, 6, 4, 1, 2], [], [-100, -85], [1, 2, 3], [1], [1, 2], [1, 1], [4, 5, 6, 2]]
    for a in A:
        res = solution(a)
        print(res)