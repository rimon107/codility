
def fibonacci(n):
    fib = [0] * (n)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def timeout_solution(A, B):
    size = len(A)
    n = max(A)
    fib = fibonacci(n+2)
    result = []
    for i in range(size):
        res = int(fib[A[i]+1] % (1 << B[i]))
        result.append(res)
    # print(result)
    return result

def fibonacci(n):
    fib = [0] * (n)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def solution(A, B):
    size = len(A)
    n = max(A)
    fib = fibonacci(n+2)
    result = []
    for i in range(size):
        res = int(fib[A[i]+1] & ((1 << B[i])-1))
        result.append(res)
    # print(result)
    return result


from timeit import timeit
from random import randint

if __name__=="__main__":
    A = [[[4, 4, 5, 5, 1], [3, 2, 4, 3, 1]],]
    
    # lst = []
    # N = 20000
    # for _ in range(N):
    #     lst.append(randint(1, N*2+1))
    for a in A:
        t1 = timeit(lambda: solution(a[0], a[1]), number=1)
        print(t1)