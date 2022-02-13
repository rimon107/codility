def solution(N):
    n_bin = format(N, "b")
    bins = n_bin.split("1")
    result = 0
    length = len(bins)
    if length>2:
        bins.pop()
        for n in bins:
            n_length = len(n) 
            if n_length > result:
                result = n_length

    return result
    

if __name__=="__main__":
    N = 51712
    N = 4641
    N = 2320
    res = solution(N)
    print(res)