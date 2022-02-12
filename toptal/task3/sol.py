from math import ceil

def solution(A):
    size = len(A)
    res_half = sum(A) / 2
    filter = 0
    A.sort(reverse=True)
    count = 0
    while True:
        total = 0
        flag = False
        first = 0
        for i in range(size-1):
            half = A[i] / 2
            if ceil(half) >= A[i+1]:
                filter += 1
                A[i] = half
                first = 1
            else:
                if first==0:
                    filter += 1
                    flag = True

                total = sum(A)
                if total <= res_half:
                    flag = True
                break
        if flag:
            break
        if count==2:
            break
        count += 1
    print(f"filter: {filter}")
    return filter
    


from timeit import timeit
from random import randint

if __name__=="__main__":
    # A = [[[4, 4, 5, 5, 1], [3, 2, 4, 3, 1]],]
    
    # A = []
    # N = 20000
    # for _ in range(N):
    #     A.append(randint(1, N*2+1))
    A = [
        [5, 19, 8, 1],
        [10, 10],
        [3, 0, 5],
    ]
    for a in A:
        t1 = timeit(lambda: solution(a), number=1)
        # print(t1)