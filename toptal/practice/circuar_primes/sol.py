from itertools import permutations

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


def permutation(A):
    perms = list(permutations(A))
    return perms

def solution(N):
    primes = sieve_prime(N)
    res = []
    count = 0
    for prime in primes:
        s_prime = str(prime)
        if len(s_prime) < 2:
            count += 1
            res.append(prime)
            continue
        lst = permutation(s_prime)
        flag = False
        lst.pop(0)
        for item in lst:
            n_prime = int("".join(item))
            if is_prime(n_prime):
                flag = True
            else:
                flag = False
        if flag:
            count += 1
            res.append(prime)
    return res, count
    
if __name__=="__main__":
    A = [100]
    for a in A:
        res, count = solution(a)
        print(res)
        print(count)