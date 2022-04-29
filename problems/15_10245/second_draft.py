import bisect

lines = [line.rstrip('\n') for line in open(
        #r'C:\Users\malek\Desktop\Advanced-Programming-Assignments\problems\15_10245\super_testcases.txt')]
        r'C:\kurser\Advanced-Programming-Assignments\problems\15_10245\super_testcases.txt')]

lines.pop()
while True:
    points = []
    number_of_points = int(lines.pop(0))
    for i in range(number_of_points): 
        temp = lines.pop(0).split()
        point = (int(temp[0]), int(temp[1]))
        points.append(point)
    #sort by x-coordinate (increasing order)
    points.sort(key=lambda p: p[0])
    # Finding closest pair for each test case
    """res = find_closest(points, number_of_points)
    if res == "inf" or res > 10000:
        print("INFINITY")
    else:
        print("{0:.4f}".format(res))"""
    if len(lines) != 0:
        continue
    break