
def solution(S):
    size = len(S)
    if size%2==1:
        return 0

    stack = []

    for e in S:
        if e=="(":
            stack.append(e)
        else:
            if not stack:
                return 0
            else:
                sl = stack.pop()
                
    if len(stack)==0:
        return 1
    return 0
    
if __name__=="__main__":
    A = ["(()(())())", "())", ]
    for a in A:
        res = solution(a)
        print(res)