import sys # importing sys library
import math # importing math library

data = sys.stdin.read().split('\n') # Read input from standard input and split it by new line

line = 0 #initializing line variable to 0
while True:
    nr_corners = int(data[line]) # assign the first line to a variable, convert it to int
    if nr_corners == 0: # if number of corners is 0, exit the loop
        break
    line += 1 # increment line by 1
    corners = [] # create an empty list named corners
    i = 0
    while i < nr_corners:
        corners.append(tuple(map(int, data[line].split()))) # map the input from the line and split it to x,y coordinates and append it to corners
        i += 1 # increment i by 1
        line += 1 # increment line by 1
    turns = 0 # initialize turns variable to 0
    u = (corners[1][0] - corners[0][0], corners[1][1] - corners[0][1]) # create a vector u using the difference between coordinates of point 1 and point 0
    v = (corners[2][0] - corners[0][0], corners[2][1] - corners[0][1]) # create a vector v using the difference between coordinates of point 2 and point 0
    cross = u[0]*v[1] - u[1]*v[0] # calculate cross product of vectors u and v
    if cross < 0:
        ref = 'Right' #if cross product is negative, set reference direction as Right
    else:
        ref = 'Left' #if cross product is positive, set reference direction as Left
    turns += 1 #increment turns by 1
    for j in range(1, len(corners) - 1): #iterate over the corners list starting from index 1 till the second last element
        u = (corners[j + 1][0] - corners[j][0], corners[j + 1][1] - corners[j][1]) # create a vector u using the difference between coordinates of next point and current point
        if j >= len(corners) - 2:
            v = (corners[0][0] - corners[j][0], corners[0][1] - corners[j][1]) # create a vector v using the difference between coordinates of first point and current point
        else:
            v = (corners[j + 2][0] - corners[j][0], corners[j + 2][1] - corners[j][1]) # create a vector v using the difference between coordinates of next next point and current point
        cross = u[0]*v[1] - u[1]*v[0] # calculate cross product of vectors u and v
        if cross < 0:
            if ref == 'Right': # check if the cross product is negative and the reference direction is Right
                turns += 1
        else:
            if ref == 'Left': # check if the cross product is positive and the reference direction is Left
                turns += 1
    u = (corners[0][0] - corners[-1][0], corners[0][1] - corners[-1][1]) # create a vector u using the difference between coordinates of first point and last point
    v = (corners[1][0] - corners[-1][0], corners[1][1] - corners[-1][1]) # create a vector v using the difference between coordinates of second point and last point
    cross = u[0]*v[1] - u[1]*v[0] # calculate cross product of vectors u and v
    if cross < 0:
        if ref == 'Right': # check if the cross product is negative and the reference direction is Right
            turns += 1
    else:
        if ref == 'Left':
            turns += 1
    if turns != nr_corners:
        print('Yes')
    else:
        print('No')