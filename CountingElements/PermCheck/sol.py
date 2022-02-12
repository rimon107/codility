def solution(A):
    # write your code in Python 3.6
    l = len(A)
    s = set(A)
    ls = len(s)
    d = 0
    if l != ls:
        return 0
    for i in s:
        d += 1
        if i!=d:
            return 0
    return 1

if __name__=="__main__":
    A = [1, 3, 4]
    res = solution(A)
    print(res)