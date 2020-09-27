class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0
        instructions = instructions*4        
        start = (0, 0)        
        for ch in instructions:
            if ch == 'G':
                start = (start[0] + dirs[dir][0], start[1] + dirs[dir][1])
                # start = newPos
            elif ch == 'L':
                dir = (dir-1)%4
            else:
                dir = (dir+1)%4
        return start[0] == 0 and start[1] == 0 and dir == 0
        