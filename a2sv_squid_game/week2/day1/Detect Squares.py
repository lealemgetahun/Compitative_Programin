class DetectSquares:

    
    def __init__(self):

        self.dic = defaultdict(int)
        self.hor = defaultdict(dict)
               
    def add(self, point: List[int]) -> None:
        x, y = point
        self.dic[(x,y)] += 1
        if y not in self.hor[x]:
            self.hor[x][y] = 0
        self.hor[x][y] += 1
               
    def count(self, point: List[int]) -> int:
        x, y = point 
        ans = 0

        for i in self.hor[x]:
            if y != i:
                temp = self.dic[(x, i)] * self.dic[(x + i - y) , y] * self.dic[(x + i - y), i]
                # print(temp, x, x + i - y)
                temp2 = self.dic[(x, i)] * self.dic[(x + y - i, y)] * self.dic[(x + y - i, i)]
                # print(temp2, x, x + y - i)
                ans += (temp + temp2)
        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)