
def solution(A):
    return len(set(map(abs, A)))
    


if __name__=="__main__":
    A = [[-5, -3, -1, 0, 3, 6],]
    for a in A:
        res = solution(a)
        print(res)