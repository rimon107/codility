def solution(A, K):
    # write your code in Python 3.6
    if len(A) > 1:
        for _ in range(K):
            item = A.pop()
            A.insert(0, item)
    return A


def another_solution(A, K):
    length = len(A)
    if length > 1:
        rotate = K % length
        if rotate != 0:
            a = A[rotate-1:length] + A[0:rotate-1]
            return a
    return A

if __name__=="__main__":
    A = []
    res = solution(A, 6)
    print(res)