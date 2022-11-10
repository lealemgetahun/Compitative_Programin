class Solution:
    # y = mx + b
    def calc_slope_interc(self, x1,y1,x2,y2):
        if y1==y2:
            return 0,y1
        if x1==x2:
            return None,x1 
        
        slope = (y2-y1)/(x2-x1)
        b = y2-slope*x2
        
        return (slope,b)
    def maxPoints(self, points: List[List[int]]) -> int: 
        if len(points)==1:
            return 1
        dic = defaultdict(set)
                
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                sl_b = self.calc_slope_interc(x1, y1, x2, y2)
                dic[sl_b].add(i)
                dic[sl_b].add(j)
        ans = 0
        for i in dic:
            ans = max(ans, len(dic[i]))

        return ans
                



