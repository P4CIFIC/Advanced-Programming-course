import math

class ClosestPair():
    def __init__(self, x_sorted_points, y_sorted_points, number_of_points) -> None:
        self.smallest_distance = "INFINITY"
        self.divide_and_conquer(x_sorted_points, y_sorted_points, number_of_points)
    
    def dist(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) * (point1[0] - point2[0]) +
                         (point1[1] - point2[1]) * (point1[1] - point2[1]))
    
    def closest_brute_force(self, points):
        min = math.inf
        number_of_points = len(points)
        for i in range(number_of_points):
            for j in range(i + 1, number_of_points):
                if self.dist(points[i], points[j]) < min:
                    min = self.dist(points[i], points[j])
        return min
    
    def closest_in_section(self, section, number_of_points, section_size):
        min = section_size
        for i in range(number_of_points):
            for j in range(i+1, number_of_points):
                if (section[j][1] - section[i][1]) > min:
                    break
                elif self.dist(section[i], section[j]) < min:
                    min = self.dist(section[i], section[j])
        return min
    
    def divide_and_conquer(self, x_sorted_points, y_sorted_points, number_of_points):
        if number_of_points <= 3:
            return self.closest_brute_force(x_sorted_points)

        mid = number_of_points//2
        mid_point = x_sorted_points[mid]
        
        points_left = x_sorted_points[:mid]
        points_right = x_sorted_points[mid:]
        
        min_left = self.divide_and_conquer(points_left, y_sorted_points, mid)
        min_right = self.divide_and_conquer(points_right, y_sorted_points, number_of_points - mid)
        min_both_sides = min(min_left, min_right)
        
        x_section = []
        y_section = []
        
        points_left_right = points_left + points_right
        for i in range(number_of_points):
            if abs(points_left_right[i][0] - mid_point[0]) < min_both_sides:
                x_section.append(points_left_right[i])
            if abs(y_sorted_points[i][0] - mid_point[0]) < min_both_sides:
                y_section.append(y_sorted_points[i])
        
        x_section.sort(key=lambda p: p[1])
        min_a = min(min_both_sides, 
                    self.closest_in_section(x_section, len(x_section), min_both_sides))
        min_b = min(min_both_sides, 
                    self.closest_in_section(y_section, len(y_section), min_both_sides))

        self.smallest_distance = min(min_a, min_b)
    
    def get_smallest_distance(self):
        if isinstance(self.smallest_distance, str):
            return self.smallest_distance
        elif isinstance(self.smallest_distance, int) or isinstance(self.smallest_distance, float):
            if self.smallest_distance < 10000:
                return("{0:.4f}".format(self.smallest_distance))
            else:
                return "INFINITY"


lines = [line.rstrip('\n') for line in open(
        r'C:\Users\malek\Desktop\Advanced-Programming-Assignments\problems\15_10245\super_testcases.txt')]
        #r'C:\kurser\Advanced-Programming-Assignments\problems\15_10245\super_testcases.txt')]
lines.pop()

while True:
    points = []
    number_of_points = int(lines.pop(0))
    for i in range(number_of_points): 
        temp = lines.pop(0).split()
        point = (int(temp[0]), int(temp[1]))
        points.append(point)
    #sort by x-coordinate (increasing)
    x_sorted_points = sorted(points, key=lambda p: p[0])
    #sort by y-coordinate (increasing)
    y_sorted_points = sorted(points, key=lambda p: p[1])
    cp = ClosestPair(x_sorted_points, y_sorted_points, number_of_points)
    print(cp.get_smallest_distance())
    if len(lines) != 0:
        continue
    break