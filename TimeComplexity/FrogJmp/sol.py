import math
def solution(X, Y, D):
    if X==Y:
        return 0
    if D==0:
        return 0
    if X+D >= Y:
        return 1
    result = 0
    distance = Y-X
    result = math.ceil(distance / D)
    return result
    

if __name__=="__main__":
    X, Y, D = 1, 1, 3
    res = solution(X, Y, D)
    print(res)