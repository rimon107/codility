from math import sqrt

def solution(N):
    i = int(sqrt(N))
    while i >= 2:
        x = N & ((1<<i)-1)
        if x==0:
            return i
        i -= 1