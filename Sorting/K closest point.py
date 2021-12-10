import math
def kClosest(points, k):
        
    dic_of_points = {}
    dic_of_distance = {}
    out = []
    for i,val in enumerate(points):
        dic_of_points[i] = val
    for i in range(len(points)):
        dis = math.sqrt(points[i][0]**2+points[i][1]**2)
        dic_of_distance[i] = dis
            
    sorted_list = sorted(dic_of_distance.items(), key=lambda item: item[1])
        
    for i in range(k):
        index = sorted_list[i][0]
        out.append(dic_of_points[index])
    return out