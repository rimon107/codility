
def solution(A):
    la = len(A)
    if la==0:
        return 1
    A.sort()
    res = 0
    p = la + 1
    for _ in range(la):
        item = A.pop()
        if item != p:
            return p
        p -= 1
    return p

if __name__=="__main__":
    A = [1, 2, 3]
    res = solution(A)
    print(res)