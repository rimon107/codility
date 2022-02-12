
def timeout_solution(A):
    size = len(A)
    stone = 1
    block = []
    a = A[0]
    block.append(a)
    min = a
    for i in range(1, size):
        if min > A[i]:
            min = A[i]
            block.clear()
            block.append(min)
        if A[i-1] != A[i]:
            if A[i-1] > A[i]:
                if block:
                    block.pop()
                    if A[i] not in block:
                        stone += 1
                        block.append(A[i])
            else:
                block.append(A[i])
                stone += 1
    return stone

def solution(H):
    block_cnt = 0
 
    stack = []
 
    for height in H:
        # remove all blocks that are bigger than my height
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
 
        if len(stack) != 0 and stack[-1] == height:
            # we already paid for this size
            pass
        else:
            # new block is required, push it's size to the stack
            block_cnt += 1
            stack.append(height)
 
    return block_cnt

if __name__=="__main__":
    A = [[8, 8, 5, 7, 9, 8, 7, 4, 8], [1]]
    for a in A:
        res = solution(a)
        print(res)