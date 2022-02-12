def solution(A):
    f = A.pop(0)
    max_ending = max_slice = f
    for a in A:
        max_ending = max(a, max_ending+a)
        max_slice = max(max_slice, max_ending)
    return max_slice


if __name__=="__main__":
    A = [[3, 2, -6, 4, 0], [3, 4, 3, 2, 3, -1, 3, 3], [-10], [-2, 1], [-2, -2]]
    for a in A:
        res = solution(a)
        print(res)