from itertools import chain

def factors(n):
    yield from chain.from_iterable(({i, n//i} for i in range(1, int(n ** 0.5) + 1) if n % i == 0))

def is_prime(n):
    if n==1:
        return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i += 1
    return True

def timeout_solution(A, B):
    size = len(A)
    res = []
    for i in range(size):
        al = []
        bl = []
        af = factors(A[i])
        for a in af:
            if is_prime(a):
                al.append(a)
        bf = factors(B[i])
        for b in bf:
            if is_prime(b):
                bl.append(b)
        res.append([al, bl])
    count = 0
    for i, e in enumerate(res):
        if len(e[0])==len(e[1]):
            e[0].sort()
            e[1].sort()
            if e[0]==e[1]:
                count += 1
    return count

def gretest_common_divisor(a, b, res=1):
    if a==b:
        return res * a
    elif a%2==0 and b%2==0:
        return gretest_common_divisor(a//2, b//2, res*2)
    elif a%2==0 :
        return gretest_common_divisor(a//2, b, res)
    elif b%2==0:
        return gretest_common_divisor(a, b//2, res)
    elif a>b:
        return gretest_common_divisor(a-b, b, res)
    else:
        return gretest_common_divisor(a, b-a, res)


def timeout_solution(A, B):
    size = len(A)
    count = 0
    for i in range(size):
        if A[i]==1 or B[i]==1:
            continue
        else:
            if A[i]==B[i]:
                count += 1
            else:
                gcd = gretest_common_divisor(A[i], B[i])
                a_gcd = A[i] / gcd
                b_gcd = B[i] / gcd
                flag_a = False
                flag_b = False
                if a_gcd==1:
                    flag_a = True
                else:
                    while True:
                        na_gcd = a_gcd / gretest_common_divisor(a_gcd, gcd)
                        if na_gcd==a_gcd:
                            flag_a = False
                            break
                        elif na_gcd==1:
                            flag_a = True
                            break
                if b_gcd==1:
                    flag_b = True
                else:
                    while True:
                        nb_gcd = b_gcd / gretest_common_divisor(b_gcd, gcd)
                        if nb_gcd==b_gcd:
                            flag_b = False
                            break
                        elif nb_gcd==1:
                            flag_b = True
                            break
                if flag_a and flag_b:
                    count += 1
    # print(count)
    return count


def gcd_division(a, b):
    if not a%b:
        return b
    return gcd_division(b, a%b)

def prime_reduce(n, gcd):
    na = n // gcd
    ngcd = gcd_division(na, gcd)
    if na == 1:
        return True # success base case
    elif ngcd == 1:
        return False
    return prime_reduce(na, ngcd)

def solution(A, B):
    Z = len(A)
    result = 0
    for i in range(0, Z):
        a, b = A[i], B[i]
        if a == b:
            result += 1
        else:
            gcd = gcd_division(a, b)
            result += (prime_reduce(a, gcd) and prime_reduce(b, gcd))
    return result


from timeit import timeit
from random import randint

if __name__=="__main__":
    A = [[[15, 10, 3], [75, 30, 5]], [[2, 1, 2], [1, 2, 2]]]
    # for a in A:
    #     res = solution(a)
        # print(res)
    
    # lst = []
    # N = 20000
    # for _ in range(N):
    #     lst.append(randint(1, N*2+1))
    for a in A:
        t1 = timeit(lambda: solution(a[0], a[1]), number=1)
        print(t1)