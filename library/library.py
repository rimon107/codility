from itertools import chain, permutations

def factors(n):
    yield from chain.from_iterable(({i, n//i} for i in range(1, int(n ** 0.5) + 1) if n % i == 0))

def sieve_prime(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    primes = []
    while (i * i <= n):
        if sieve[i]:
            k = i * i
            while (k <= n):
                sieve[k] = False
                k += i
        i += 1
    for i, item in enumerate(sieve):
        if item:
            primes.append(i)
    return primes



def is_prime(n):
    if n==1:
        return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i += 1
    return True

def fibonacci(n):
    fib = [0] * (n)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def gcd_division(a, b):
    if not a%b:
        return b
    return gcd_division(b, a%b)

def permutation(A):
    perms = list(permutations(A))
    return perms

if __name__=="__main__":
    # A = [[1,2,3], "abc", 123]
    # for a in A:
    #     res = permutation(a)
    #     print(res)
    A = [100]
    for a in A:
        res = sieve_prime(a)
        print(res)
        print(len(res))