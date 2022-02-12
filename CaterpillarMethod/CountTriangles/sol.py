from collections import Counter

def solution(A):
    size = len(A)
    count = 0
    cnt = Counter(A)
    if size<3:
        return 0
    else:
        A = list(set(A))
        print(A)
        # A.sort()
        print(A)
        l = len(A)
        if l>=3:
            for i in range(l-1,1, -1):
                if A[i-1] + A[i-2] >= A[i]:
                    count += 1
                    print(f"count: {count}")
                    # else:
                    #     break
    return count

if __name__=="__main__":
    A = [[10, 2, 5, 1, 8, 12],[20, 1, 1], [3, 3, 5, 6]]
    for a in A:
        res = solution(a)
        print(res)