import math

class ClosestPair():
    def __init__(self, all_points, number_of_points, test_case) -> None:
        #sort by x-coordinate (increasing)
        self.x_sorted_points = sorted(all_points, key=lambda p: p[0])
        #sort by y-coordinate (increasing)
        self.y_sorted_points = sorted(all_points, key=lambda p: p[1])
        self.number_of_points = number_of_points
        
        visited = set()
        dups = []
        for a, b in self.x_sorted_points:
            if a in visited:
                dups.append(a)
            else:
                visited.add(a)
        print(dups)
        pass
        #self.divide_and_conquer()
        #pass
    
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
    
    def closest_in_section(self, section, section_size):
        min = section_size
        for i in range(self.number_of_points):
            for j in range(i+1, self.number_of_points):
                if (section[j][1] - section[i][1]) > min:
                    break
                elif self.dist(section[i], section[j]) < min:
                    min = self.dist(section[i], section[j])
        return min
    
    def divide_and_conquer(self):
        if self.number_of_points <= 3:
            return self.closest_brute_force(self.x_sorted_points)
        mid = self.number_of_points
        mid_point = self.x_sorted_points[mid]
        
        
            
    
    

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

    res = ClosestPair(points, number_of_points)
    """if res > 10000:
        print("INFINITY")
    else:
        print("{0:.4f}".format(res))"""
    if len(lines) != 0:
        continue
    break