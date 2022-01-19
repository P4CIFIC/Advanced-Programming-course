import math

class Point():
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    #For debugging 
    def __repr__(self) -> str:
        return (f"x:{self.x} y:{self.y}")

#returns the variables k and m from "y = kx + m"
def get_lin_equation(point_a, point_b):
    k = (point_a.y - point_b.y)/(point_a.x - point_b.x)
    m = point_a.y - (k * point_a.x)
    return k, m

def get_x (point, k, m):
    return (point.y-m) / k

def get_distance(point_a, point_b):
    return math.sqrt( ((point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2) )

#function that creates the pairs of points that intersect 
def find_intersections(coordinates, n):
    distance = 0
    peak_1 = coordinates[0]
    peak_2 = coordinates[0]
    for i, point in enumerate(coordinates):
        try: 
            if coordinates[i].y > peak_1.y:
                peak_2 = peak_1
                peak_1 = coordinates[i]
                
                if peak_2.y != 0:
                    peak_1_friend = coordinates[i-1]
                    k, m = get_lin_equation(peak_1, peak_1_friend)
                    x = get_x(peak_2, k, m)
                    distance += math.hypot(peak_1.x - x, peak_1.y - peak_2.y)
        except IndexError:
            break
    print(distance)
    
# Reading the dataset and creating Points, assigning 'x' and 'y' to the 
# instance variables of the different Point objects.   
number_of_test_cases = int(input())
for n in range(number_of_test_cases):
    print(f"Testcase: {n+1}")
    coordinates = []            # list for all points
    number_of_points = int(input())
    for i in range (number_of_points):
        temp = input().split()
        point = Point(int(temp[0]), int(temp[1]))
        coordinates.append(point)
        number_of_points = len(coordinates)
    # Sorting the points in list (coordinates) by 'x' value in ascending order  
    coordinates.sort(key=lambda x: x.x, reverse=True)
    find_intersections(coordinates, number_of_points)
    #print(answer)
    
    ## here goes the rest of code for analyzing etc
    #print(f"{coordinates}")