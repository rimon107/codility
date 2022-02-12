from collections import Counter

def solution(A):
    size = len(A)
    if size > 0:
        cnt = Counter(A)
        dominator = cnt.most_common(1)
        occurance = dominator[0][1] 
        if occurance > size//2:
            i = dominator[0][0] 
            return A.index(i)
    return -1


if __name__=="__main__":
    A = [[3, 4, 3, 2, 3, -1, 3, 3],]
    for a in A:
        res = solution(a)
        print(res)