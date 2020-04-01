class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir1, dir2 = 0, 0
        for ch in moves:
            if ch == 'U':
                dir1 += 1
            elif ch == 'D':
                dir1 -= 1
            elif ch == 'R':
                dir2 += 1
            elif ch == 'L':
                dir2 -= 1
                
        if dir1 == 0 and dir2 == 0:
            return True
        else:
            return False
        