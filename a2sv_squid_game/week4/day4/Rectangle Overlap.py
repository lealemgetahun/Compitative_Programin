class Solution:
    def intersection(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
        x = max(min(ax2,bx2) - max(ax1,bx1),0) , max(min(ay2,by2) - max(ay1,by1),0)
        return x

    def area(self, x1, x2, y1, y2):
        x = abs(x1 - x2)
        y = abs(y1 -y2)

        return x*y
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1,ay1,ax2,ay2 = rec1
        bx1,by1,bx2,by2 = rec2

        x_int, y_int = self.intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        
        intersection_area = x_int * y_int
      
        return intersection_area > 0