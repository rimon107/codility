def solution(X, A):
    i=0
    check = [1] * (X+1)
    size = len(A)
    start = 0
    slices = []
    for i in range(size):
        if check[A[i]]==0:
            slices.append([start, i-1])
            start = i
        if check[A[i]]==1:
            check[A[i]] = 0
        if i==size-1:
            slices.append([start, i])
    # print(slices)
    count = 0
    for slice in slices:
        n = (slice[1] - slice[0]) + 1
        sum = (n * (n+1)) // 2
        count += sum
    return count
    


if __name__=="__main__":
    A = [[6, [3, 4, 5, 5, 2]], [100000, [1, 1]]]
    for a in A:
        res = solution(a[0], a[1])
        print(res)