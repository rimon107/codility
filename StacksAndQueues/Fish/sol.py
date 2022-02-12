
def not_solution(A, B):
    res = 0
    size = len(A)
    alive = [1] * size
    next = []
    for index, item in enumerate(B):
        if item==1:
            next.append(index)

    if len(next)==0 or len(next)==size:
        return size 
    act = 0
    for _ in range(size-1):
        if act==-1 or act==size:
            break
        if B[act] and B[act]==0:
            if act-1 < 0:
                while act!=size:
                    if B[act] and B[act]==1:
                        break
                    act += 1
                if act==size:
                    break
            else:
                if B[act-1] and B[act-1]==0:
                    act -= 1
                else:
                    if A[act] and A[act-1]:
                        if A[act] > A[act-1]:
                            alive[act-1] = 0
                            B[act] = None
                            B[act-1] = 0
                            A[act-1] = A[act]
                            A[act] = None
                            act -= 1
                        else:
                            alive[act] = 0
                            B[act-1] = None
                            B[act] = 1
                            A[act] = A[act-1]
                            A[act-1] = None
                            act += 1
        elif B[act]==1:
            if act == size-1:
                while act!=-1:
                    if B[act] and B[act]==0:
                        break
                    act -= 1
                if act==-1:
                    break
            else:
                if B[act+1] and B[act+1]==1:
                    act += 1
                else:
                    if A[act] and A[act+1]:
                        if A[act] > A[act+1]:
                            alive[act+1] = 0
                            B[act] = None
                            B[act+1] = 1
                            A[act+1] = A[act]
                            A[act] = None
                            act += 1
                        else:
                            alive[act] = 0
                            B[act+1] = None
                            B[act] = 0
                            A[act] = A[act+1]
                            A[act+1] = None
                            act -= 1

    res = sum(alive)
    return res

def solution(A, B):
    res = 0
    size = len(A)
    next = []
    up = []
    down = []
    for index, item in enumerate(B):
        if item==1:
            next.append(index)

    if len(next)==0 or len(next)==size:
        return size
    i = 0
    while True:
        if A[i]:
            if B[i]==1:
                    down.append([A[i], i])
            else:
                if not down:
                    up.append([A[i], i])
                else:
                    w = down.pop()
                    if w[0] < A[i]:
                        while True:
                            if down:
                                p = down.pop()
                                if p[0] > A[i]:
                                    down.append(p)
                                    break
                            else:
                                up.append([A[i], i])
                                break
                    else:
                        down.append(w)
            i += 1
            if i==size:
                break
    res = len(up) + len(down)
    return res

if __name__=="__main__":
    input_list = [[[4, 3, 2, 1, 5], [0, 1, 0, 0, 0]], [[0, 1], [1, 1]], [[4, 3, 2, 6, 5], [1, 1, 0, 0, 0]]]
    for input in input_list:
        A = input[0]
        B = input[1]
        res = solution(A, B)
        print(res)