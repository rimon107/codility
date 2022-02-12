def solution(E, L):
    e_time = E.split(":")
    l_time = L.split(":")

    hours = int(l_time[0])-int(e_time[0])

    if hours>0:
        hours -= 1

    if int(l_time[1]) > int(e_time[1]):
        if l_time[0]!=e_time[0]:
            hours += 1

    cost = 2+3+(hours*4)
    return cost