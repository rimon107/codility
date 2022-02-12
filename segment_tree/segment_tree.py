# function to build the segmenttree array
from sys import maxsize

def build(input, n):
    tree = [None] * 2 * n
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = input[i]

    # creating parent node by adding left and right child
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]
    return tree

# function to update a node of the tree
def update(tree, size, index, value):
    # set value at position index 
    tree[index + size] = value
    index+=size

    # after updating the child node,update parents
    i = index

    while i > 1: 
    #update parent by adding new left and right child
        tree[i//2] = tree[i] + tree[i+1]
        i =i//2
    return tree

#function to find sum on different range 
def range_sum(tree, size, left, right):
    sum = 0
    left += size
    right += size

    while left < right:
        if ((left & 1)>0):
            sum += tree[left]
            left += 1
        if ((right & 1)>0):
            right -= 1
            sum += tree[right]
        left =left// 2
        right = right// 2

    return sum

def max_contiguous_sum(input, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(size):
        max_ending_here = max_ending_here + input[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0  
            s = i+1
    return max_so_far, start, end
    
def segment_tree():
    input = [1, 3, -2, 8, -7]
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    length = len(input)
    tree = build(input, length)
    print(tree)
    s = range_sum(tree, length, 2, 4)
    print(s)

if __name__=="__main__":
    segment_tree()