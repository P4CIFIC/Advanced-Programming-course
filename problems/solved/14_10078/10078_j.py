import sys
import math


data = sys.stdin.read().split('\n')


line = 0
while True:
    nr_corners = int(data[line])
    if nr_corners == 0:
        break
    line += 1
    corners = []
    i = 0
    while i < nr_corners:
        corners.append(tuple(map(int, data[line].split())))
        i += 1
        line += 1
    turns = 0
    u = (corners[1][0] - corners[0][0], corners[1][1] - corners[0][1])
    v = (corners[2][0] - corners[0][0], corners[2][1] - corners[0][1])
    cross = u[0]*v[1] - u[1]*v[0]
    if cross < 0:
        ref = 'Right'
    else:
        ref = 'Left'
    turns += 1
    for j in range(1, len(corners) - 1):
        u = (corners[j + 1][0] - corners[j][0],
             corners[j + 1][1] - corners[j][1])
        if j >= len(corners) - 2:
            v = (corners[0][0] - corners[j][0],
                 corners[0][1] - corners[j][1])
        else:
            v = (corners[j + 2][0] - corners[j][0],
                 corners[j + 2][1] - corners[j][1])
        cross = u[0]*v[1] - u[1]*v[0]
        if cross < 0:
            if ref == 'Right':
                turns += 1
        else:
            if ref == 'Left':
                turns += 1

    u = (corners[0][0] - corners[-1][0], corners[0][1] - corners[-1][1])
    v = (corners[1][0] - corners[-1][0], corners[1][1] - corners[-1][1])
    cross = u[0]*v[1] - u[1]*v[0]
    if cross < 0:
        if ref == 'Right':
            turns += 1
    else:
        if ref == 'Left':
            turns += 1
    if turns != nr_corners:
        print('Yes')
    else:
        print('No')
