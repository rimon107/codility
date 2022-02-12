# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(S):
    size = len(S)
    count = Counter(S)
    a_count = count.get('a', 0)
    b_count = count.get('b', 0)

    as_lists = []
    bs_lists = []

    if a_count<3 or b_count <3:
        return -1

    for i, item in enumerate(S):
        if item=='a':
            as_lists.append(i)
        else:
            bs_lists.append(i)

    a_found = False
    as_length = len(as_lists)
    for i in range(as_length-2):
        if as_lists[i]+1==as_lists[i+1] and as_lists[i+1]+1==as_lists[i+2]:
            a_found = True
            break
    b_found = False
    bs_length = len(bs_lists)
    for i in range(bs_length-2):
        if bs_lists[i]+1==bs_lists[i+1] and bs_lists[i+1]+1==bs_lists[i+2]:
            b_found = True
            break

    if a_found and b_found:
        return 0

    if a_found:
        min_dis = size+1
        min_index = -1
        max_dis = -1
        max_index = -1
        for i in range(bs_length-1):
            dis = bs_lists[i+1] - bs_lists[i]
            if dis < min_dis:
                min_dis = dis
                min_index = bs_lists[i]
            if dis > max_dis:
                max_dis = dis
                max_index = bs_lists[i]
        return (max_dis-1) + (min_dis-1)
        
    if b_found:
        min_dis = size+1
        min_index = -1
        max_dis = -1
        max_index = -1
        for i in range(as_length-1):
            dis = as_lists[i+1] - as_lists[i]
            if dis < min_dis:
                min_dis = dis
                min_index = as_lists[i]
            if dis > max_dis:
                max_dis = dis
                max_index = as_lists[i]
        return (max_dis-1) + (min_dis-1)
    a_dis = 0
    b_dis = 0
    if as_lists[0]==0:
        min_dis = size+1
        min_index = -1
        max_dis = -1
        max_index = -1
        for i in range(as_length-1):
            dis = as_lists[i+1] - as_lists[i]
            if dis < min_dis:
                min_dis = dis
                min_index = as_lists[i]
            if dis > max_dis:
                max_dis = dis
                max_index = as_lists[i]
        a_dis = (max_dis-1) + (min_dis)
        if min_index > max_index:
            min_dis = size+1
            min_index = -1
            max_dis = -1
            max_index = -1
            for i in range(bs_length-1):
                dis = bs_lists[i+1] - bs_lists[i]
                if dis < min_dis:
                    min_dis = dis
                    min_index = bs_lists[i]
                if dis > max_dis:
                    max_dis = dis
                    max_index = bs_lists[i]
            
            b_dis = (max_dis-1) + (min_dis)
            return b_dis
        else:
            return a_dis
    else:
        min_dis = size+1
        min_index = -1
        max_dis = -1
        max_index = -1
        for i in range(bs_length-1):
            dis = bs_lists[i+1] - bs_lists[i]
            if dis < min_dis:
                min_dis = dis
                min_index = bs_lists[i]
            if dis > max_dis:
                max_dis = dis
                max_index = bs_lists[i]
        b_dis = (max_dis-1) + (min_dis)
        if min_index > max_index:
            min_dis = size+1
            min_index = -1
            max_dis = -1
            max_index = -1
            for i in range(as_length-1):
                dis = as_lists[i+1] - as_lists[i]
                if dis < min_dis:
                    min_dis = dis
                    min_index = as_lists[i]
                if dis > max_dis:
                    max_dis = dis
                    max_index = as_lists[i]
            a_dis = (max_dis-1) + (min_dis)
            return a_dis
        else:
            return b_dis


if __name__=="__main__":
    A = [
        "ababab",
        "abbabb",
        "aabb",
        "aaabb",
        "bbbababaaa",
        "ababaab",
        "aababaab"
        ]
    for a in A:
        res = solution(a)
        print(res)