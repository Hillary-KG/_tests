import math
import random


def bruteforce(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax - 1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_closest_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return bruteforce(ax)
    mid = ln_ax // 2
    Qx = ax[:mid]  # 2-part split
    Rx = ax[mid:]
    midpoint = ax[mid][0] # get midpoint on x-axis
    Qy = list()
    Ry = list()
    for x in ay:
        if x[0] <= midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
    # Call recursively both arrays after split
    (p1, q1, mi1) = get_closest_pair(Qx, Qy)
    (p2, q2, mi2) = get_closest_pair(Rx, Ry)
    # get smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    (p3, q3, mi3) = get_closest_split_pair(ax, ay, d, mn) # get points on the boundary
    if d <= mi3: # get smallest distance for the array
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def get_closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  # assign best value to delta
    ln_y = len(s_y)
    for i in range(ln_y - 1):
        for j in range(i + 1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


def get_pair(tuple_list):
    ax = sorted(tuple_list, key=lambda x: x[0])  # Presort x-wise
    ay = sorted(tuple_list, key=lambda x: x[1])  # Presort y-wise
    # Recursive D&C function
    p1, p2, mi = get_closest_pair(ax, ay)
    return p1, p2, mi
