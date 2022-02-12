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


    
def solution(message, K):
    word_list = message.split(" ")
    length = 0
    msg_list = []
    for word in word_list:
        print(length)
        print(word)
        length += len(word)
        if length <= K:
            msg_list.append(word)
            length += 1
        else:
            break
        print(length)

    result = " ".join(msg_list)
    return result
    


from timeit import timeit
from random import randint

if __name__=="__main__":
    # A = [[[4, 4, 5, 5, 1], [3, 2, 4, 3, 1]],]
    
    # A = []
    # N = 20000
    # for _ in range(N):
    #     A.append(randint(1, N*2+1))
    A = [
        ["Codality We Test Coders", 14], 
        ["Why Not", 100], 
        ["the quick brown fox jumps over the lazy dog", 39],
        ["to crop or not to crop", 21],
        ["to", 1],
    ]
    for a in A:
        t1 = timeit(lambda: solution(a[0], a[1]), number=1)
        print(t1)