import numpy as np

def find_closest_brute_force(array):
    
    result = {}
    result["p1"] = array[0]
    result["p2"] = array[1]
    result["distance"] = np.sqrt((array[0][0]-array[1][0])**2
                                +(array[0][1]-array[1][1])**2)
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            distance = np.sqrt((array[i][0]-array[j][0])**2
                              +(array[i][1]-array[j][1])**2)
            if distance < result["distance"]:
                result["p1"] = array[i]
                result["p2"] = array[j]
                result["distance"] = distance
    return result

def merge_sort(array, coordinate=0):
    
    length = len(array)
    if length == 1:
        return array
    if length == 2:
        if array[0][coordinate] > array[1][coordinate]:
            return np.array([array[1], array[0]])
        else:
            return array
    
    elif length > 2:
        array_l = array[:length//2]
        array_r = array[length//2:]
        array_l_sorted = merge_sort(array_l, coordinate)
        array_r_sorted = merge_sort(array_r, coordinate)
        
        l_length = len(array_l)
        r_length = len(array_r)
        l = 0
        r = 0
        
        sorted_list = []
        
        for i in range(length):
            if r == r_length:
                sorted_list.append(array_l_sorted[l])
                l += 1
            elif l == l_length:
                sorted_list.append(array_r_sorted[r])
                r += 1             
                
            elif array_l_sorted[l][coordinate] > array_r_sorted[r][coordinate]:
                sorted_list.append(array_r_sorted[r])
                r += 1
                
            elif array_l_sorted[l][coordinate] < array_r_sorted[r][coordinate]:
                sorted_list.append(array_l_sorted[l])
                l += 1
        
        return np.array(sorted_list)

def find_closest_nest(array):
    X = merge_sort(array, 0)
    length = len(X)
    if length < 4:
        return find_closest_brute_force(array)
    
    else:
        array_l = X[:length//2]
        array_r = X[length//2:]
        dict_l = find_closest_nest(array_l)
        dict_r = find_closest_nest(array_r)
                    
        if dict_l["distance"] > dict_r["distance"]:
            dict_both = dict_r
        else:
            dict_both = dict_l
          
        Y_list = []
        for i in range(length):
            if X[length//2-1][0]-dict_both["distance"] < array[i][0] < X[length//2-1][0]+dict_both["distance"]:
                Y_list.append(array[i])
        Y = merge_sort(np.array(Y_list), 1)
      
        
        if len(Y) == 1:
            dict_final = dict_both
        elif len(Y) < 8:
            dict_y = find_closest_brute_force(Y)
            if dict_both["distance"] > dict_y["distance"]:
                dict_final = dict_y
            else:
                dict_final = dict_both            
        else:
            for i in range(len(Y)-7):
                dict_y = find_closest_brute_force(Y[i:i+7])        
                
                if dict_both["distance"] > dict_y["distance"]:
                    dict_final = dict_y
                else:
                    dict_final = dict_both
    
        return dict_final