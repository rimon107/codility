from collections import Counter

def solution(A):
    count_dict = Counter(A)
    res = 0
    count_dict.items()
    for item in count_dict.items():
        if item[1]%2 == 1:
            res = item[0]
    return res 


if __name__=="__main__":
    A = [9, 3, 9, 3, 9, 7, 9]
    res = solution(A)
    print(res)