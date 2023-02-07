class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        pos = [0, 0]
        dirc = (0, 1)

        for ins in instructions:
            if ins == "G":
                pos[0] += dirc[0]
                pos[1] += dirc[1]
            elif ins == "L":
                if dirc == (0, 1):
                    dirc = (-1, 0)
                elif dirc == (-1, 0):
                    dirc = (0, -1)
                elif dirc == (0, -1):
                    dirc = (1, 0)
                else:
                    dirc = (0, 1)
            else:
                if dirc == (0, 1):
                    dirc = (1, 0)
                elif dirc == (1, 0):
                    dirc = (0, -1)
                elif dirc == (0, -1):
                    dirc = (-1, 0)
                else:
                    dirc = (0, 1)
    
        return pos == [0, 0] or dirc != (0, 1)
        
            

    

