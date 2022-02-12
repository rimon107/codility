from sys import maxsize

def not_all_cases_solution(A):
    size = len(A)
    prefix_sum = [0] * (size+1)
    pos = 0
    min_avg = maxsize
    min_pos = -1
    for i in range(1, size+1):
        prefix_sum[i] = prefix_sum[i-1] + A[i-1]
    for i in range(size):
        avr = (prefix_sum[i+1] - prefix_sum[pos] + A[pos]) / (i - pos + 1)
        if avr < min_avg:
            min_avg = avr
            min_pos = pos
        if A[i] < min_avg:
            pos = i
    return min_pos

def solution(A):
    size = len(A)
    prefix_sum2 = [0] * size
    prefix_sum3 = [0] * size
    min_avg = maxsize
    min_pos = -1
    s = 0
    for i in range(1, size):
        s = A[i-1] + A[i]
        prefix_sum2[i] = s

    for i in range(2, size):
        s = A[i-2] + A[i-1] + A[i]
        prefix_sum3[i] = s

    for i in range(1, size):
        avg = prefix_sum2[i]/2
        if avg < min_avg:
            min_avg = avg
            min_pos = i-1

    for i in range(2, size):
        avg = prefix_sum3[i]/3
        if avg < min_avg:
            min_avg = avg
            min_pos = i-2
    return min_pos


if __name__=="__main__":
    A = [[4, 5, 2, 2, 5, 3, 1, 2, 8], [-3, -5, -8, -4, -10]]
    for a in A:
        res = solution(a)
        print(res)