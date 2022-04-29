import math, copy

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) +
                     (p1.y - p2.y) * (p1.y - p2.y))

def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
    return min_val

def stripClosest(strip, size, d):

    min_val = d

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val

def closestUtil(P, Q, n):

    if n <= 3:
        return bruteForce(P, n)

    mid = n // 2
    midPoint = P[mid]

    Pl = P[:mid]
    Pr = P[mid:]

    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)

    d = min(dl, dr)

    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])

    stripP.sort(key=lambda point: point.y)
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))

    return min(min_a, min_b)

def closest(P, n):
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)

    return closestUtil(P, Q, n)

lines = []
"""while True:  # storing the input in a list
    line = input()
    if line == "0":
        break
    else:
        lines.append(line)
"""
lines = [line.rstrip('\n') for line in open(
        #r'C:\Users\malek\Desktop\Advanced-Programming-Assignments\problems\15_10245\super_testcases.txt')]
        r'C:\kurser\Advanced-Programming-Assignments\problems\15_10245\super_testcases.txt')]

lines.pop()

while True:
    points = []
    number_of_points = int(lines.pop(0))
    for i in range(number_of_points):  # Creating point objects for all points in test case
        temp = lines.pop(0).split()
        x, y = int(temp[0]), int(temp[1])
        point = Point(x, y)
        points.append(point)

    # Finding closest pair for each test case
    res = closest(points, number_of_points)
    if res == "inf" or res > 10000:
        print("INFINITY")
    else:
        print("{0:.4f}".format(res))
    if len(lines) != 0:
        continue
    break