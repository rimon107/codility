def solution(A, K):
    # write your code in Python 3.6
    if len(A) > 1:
        for _ in range(K):
            item = A.pop()
            A.insert(0, item)
    return A


if __name__=="__main__":
    A = []
    res = solution(A, 6)
    print(res)