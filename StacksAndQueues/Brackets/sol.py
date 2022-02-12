
def solution(S):
    open = {
        '(': 0, 
        '{': 1, 
        '[': 2
        }

    close = {
        ')': 0, 
        '}': 1, 
        ']': 2
        }

    stack = []

    for i, e in enumerate(S):
        if e in open:
            stack.append(open[e])
        else:
            last = close[e]
            if not stack:
                return 0
            else:
                sl = stack.pop()
                if sl != last:
                    return 0
                
    if len(stack)==0:
        return 1
    return 0
    
if __name__=="__main__":
    A = ["{[()()]}", "([)()]", ")(", ]
    for a in A:
        res = solution(a)
        print(res)