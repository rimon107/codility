from collections import Counter
from itertools import chain

def timeout_solution(A):
    l = len(A)
    s = Counter(A)
    result = []
    d = {}
    for i in range(l):
        if i in d:
            result.append(d[i])
        else:
            count = 0
            for key, value in s.items():
                if A[i]%key!=0:
                    count += value
            d[i] = count
            result.append(count)
    return result

def timeout_2_solution(A):
    l = len(A)
    s = Counter(A)
    result = []
    d = {}
    for i in range(l):
        if i in d:
            result.append(d[i])
        else:
            count = 0
            for key, value in s.items():
                if A[i]%key!=0:
                    count += value
            d[i] = count
            result.append(count)
    return result

from collections import Counter
from itertools import chain
def factors(n):
    yield from chain.from_iterable(({i, n//i} for i in range(1, int(n ** 0.5) + 1) if n % i == 0))

def solution(lst):
    c = Counter(lst)
    d = {val: sum((-c.get(f, 0) for f in factors(val)), len(lst)) for val in c}
    return [d[i] for i in lst]

from timeit import timeit
from random import randint

if __name__=="__main__":
    A = [[3, 1, 2, 3, 6], [1]]
    # for a in A:
    #     res = solution(a)
        # print(res)
    
    lst = []
    N = 20000
    for _ in range(N):
        lst.append(randint(1, N*2+1))

    t1 = timeit(lambda: solution(A[0]), number=1)
    print(t1)