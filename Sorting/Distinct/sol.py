
def solution(A):
    s = set(A)
    return len(s)


if __name__=="__main__":
    A = [[0, 1, 0, 1, 1],]
    for a in A:
        res = solution(a)
        print(res)