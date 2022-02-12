def timeout_solution(N, A):
    cnt = [0] * N
    max = 0
    for e in A:
        if e > N:
            cnt = list(map(lambda x: max, cnt))
        else:
            cnt[e-1] += 1
            if cnt[e-1] > max:
                max = cnt[e-1]
    return cnt 

def timeout_2_solution(N, A):
    cnt = [0] * N
    max = 0
    for e in A:
        if e > N:
            cnt = [max] * N
        else:
            cnt[e-1] += 1
            if cnt[e-1] > max:
                max = cnt[e-1]
    return cnt 

def timeout_3_solution(N, A):
    cnt = [0] * N
    max = 0
    for e in A:
        if e > N:
            for i in range(N):
                cnt[i] = max
        else:
            cnt[e-1] += 1
            if cnt[e-1] > max:
                max = cnt[e-1]
    return cnt 

def faltu_solution(N, A):
    cnt = [0] * N
    max = 0
    i = -1
    l = len(A) - 1
    flag = False

    while True:
        while i < l:
            flag = False
            i += 1
            if A[i] > N:
                flag = True
                break
            else:
                cnt[A[i]-1] += 1
                if cnt[A[i]-1] > max:
                    max = cnt[A[i]-1]
            
        if flag:
            for m in range(N):
                cnt[m] = max
        else:
            break

    return cnt 

def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for K,X in enumerate(A): # O(M)
        if 1 <= X <= N:
            counters[X-1] = max(counters[X-1], last_update)
            counters[X-1] += 1
            max_counter = max(counters[X-1], max_counter)
        elif A[K] == (N + 1):
            last_update = max_counter

    for i in range(N): # O(N)
        counters[i] = max(counters[i], last_update)

    return counters

if __name__=="__main__":
    A = [3, 4, 4, 6, 1, 4, 4]
    N = 5
    res = solution(N, A)
    print(res)