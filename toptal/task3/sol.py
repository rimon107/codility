from sys import maxsize

def solution(A):
    size = len(A)
    res_half = sum(A) / 2
    filter = 0
    A.sort(reverse=True)
    count = 0
    while True:
        total = 0
        flag = False
        for i in range(size-1):
            if A[i]==0:
                continue
            if A[i] > A[i+1]:
                filter += 1
                A[i] = A[i] / 2
                total = sum(A)
                if total <= res_half:
                    flag = True
                break
            if A[i] == A[i+1]:
                filter += 2
                A[i] = A[i] / 2
                A[i+1] = A[i+1] / 2
                total = sum(A)
                if total <= res_half:
                    flag = True
                break
            else:
                total = sum(A)
                if total <= res_half:
                    flag = True
                    break
        if flag:
            break
        if count==maxsize:
            break
        count += 1
    print(filter)
    return filter
    


from timeit import timeit
from random import randint

if __name__=="__main__":
    A = [
        [5, 19, 8, 1],
        [10, 10],
        [3, 0, 5],
    ]
    for a in A:
        t1 = timeit(lambda: solution(a), number=1)
        # print(t1)