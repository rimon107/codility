
def timeout_solution(A, B, K):
    count = 0
    for i in range(A, B+1):
        if i%K==0:
            count += 1
    return count

def not_solution(A, B, K):
    count = 0
    if K==1:
        return B-A+1
    z = 0
    if A==0:
        count += 1
        A += 1
    if A<=B:
        while True:
            if A%K==0:
                count += 1
                break
            z += 1
            A += 1
            if z==B:
                break
        i = A
        for _ in range(A, B+1):
            if i+K > B:
                break
            else:
                count += 1
                i += K
    return count

def solution(A, B, K):
    if A % K == 0:  
        return (B - A) // K + 1
    else:   
        return (B - (A - A % K )) // K

if __name__=="__main__":
    A, B, K = 7, 11, 2
    # A, B, K = 0, 2000000000, 1
    # A, B, K = 0, 15, 10
    # A, B, K = 11, 14, 2
    # A, B, K = 11, 345, 17
    # A, B, K = 0, 0, 11
    # A, B, K = 0, 1, 11
    # A, B, K = 1, 1, 11
    # A, B, K = 100, 123000000, 2
    # A, B, K = 10, 10, 5
    # A, B, K = 10, 10, 7
    # A, B, K = 10, 10, 20
    
    res = solution(A, B, K)
    print(res)