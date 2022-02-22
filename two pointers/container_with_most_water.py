def maxArea(self, height) -> int:
    i = 0
    j = len(height) -1
    max_h = 0
    while i < j:
        max_h= max( min(height[i],height[j])*(j-i),max_h)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_h