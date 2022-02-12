
def timeout_solution(A):
    intersection = 0
    size = len(A)
    calculate = []
    for i in range(size):
        l = [False] * size
        calculate.append(l)
    
    for i in range(size):
        if A[i] > 0:
            max = i + A[i]
            min = i - A[i]
            for j in range(i+1, size):
                if not calculate[j][i]:
                    if A[j] > 0:
                        j_min = j - A[j]
                        if max >= j_min:
                            intersection += 1
                            calculate[j][i] = True
                            calculate[i][j] = True
                    else:
                        if max >= j:
                            intersection += 1
                            calculate[j][i] = True
                            calculate[i][j] = True
                        
            for k in range(i-1, -1, -1):
                if not calculate[k][i]:
                    if A[k] > 0:
                        k_max = k + A[k]
                        if k_max >= min:
                            intersection += 1
                            calculate[i][k] = True
                            calculate[k][i] = True
                        else:
                            if k >= min:
                                intersection += 1
                                calculate[j][i] = True
                                calculate[i][j] = True
    if intersection > 10000000:
        intersection = -1
    return intersection


def solution(A):
    size = len(A)
    result = 0
    dps = [0] * size
    dpe = [0] * size

    t = size - 1
    for i in range(size):
        s = i - A[i] if i > A[i] else 0
        e = i + A[i] if t - i > A[i] else t
        dps[s] += 1
        dpe[e] += 1
    print(dps)
    print(dpe)
    t = 0 #disk_in
    for i in range(size):
        if dps[i] > 0:
            result += t * dps[i]
            result += dps[i] * (dps[i] - 1) // 2
            if result > 10000000:
                return -1
            t += dps[i]
        t -= dpe[i]
        print(f"t: {t}")
        print(result)
       
    return result


if __name__=="__main__":
    A = [[1, 5, 2, 1, 4, 0], ]
    for a in A:
        res = solution(a)
        print(res)