
def solution(P, S):

    total_people = sum(P)
    total_seats = sum(S)
    total_avail = total_seats - total_people
    cars = S.copy()
    cars.sort()
    S.sort()

    for seats in S:
        if seats <= total_avail:
            total_avail -= seats
            cars.pop(0)
        else:
            break
    return len(cars)
    


from timeit import timeit
from random import randint

if __name__=="__main__":
    # A = [[[4, 4, 5, 5, 1], [3, 2, 4, 3, 1]],]
    
    # A = []
    # N = 20000
    # for _ in range(N):
    #     A.append(randint(1, N*2+1))
    A = [
        # [[1, 4, 1], [1, 5, 1]],
        # [[4, 4, 2, 4], [5, 5, 2, 5]],
        [[2, 3, 4, 2], [2, 5, 7, 2]],
    ]
    for a in A:
        t1 = timeit(lambda: solution(a[0], a[1]), number=1)
        # print(t1)