class Solution:
    def check(self, i, j, grid, motion, valid, visited):
        m, n  = len(grid), len(grid[0]) 
        count = 0
        while(i <= m-1 and j <= n-1 and i >= 0 and j >= 0 and count <= m*n):
            direction = grid[i][j]
            visited.append((i, j))          

            if (motion, direction) in valid.keys():
                j += valid[(motion,direction)][1]
                i += valid[(motion,direction)][0]
                motion = valid[(motion,direction)][2]
                if i == m-1 and j == n-1 and (motion,grid[i][j]) in valid.keys():
                    break
                elif i == m-1 and j == n-1 and (motion,grid[i][j]) not in valid.keys():
                    i += 100
                    break
                count += 1
            else:
                break

        if i == m-1 and j == n-1:
            return True
        else:
            return False
        
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = [(0,0)]
        prev = -1
        m, n  = len(grid), len(grid[0]) 
        if m == 1 and n == 1:
            return True
        i, j = 0, 0
        valid = {('l', 1):(0,-1,'l'), ('r',1):(0,1,'r'), 
                 ('d',2):(1,0,'d'), ('t',2):(-1,0,'t'),
                 ('r',3):(1,0,'d'),('t',3):(0,-1,'l'),
                 ('l',4):(1,0,'d'),('t',4):(0,1,'r'),
                 ('d', 5):(0,-1,'l'),('r',5):(-1,0,'t'),
                 ('d',6):(0,1,'r'),('l',6):(-1,0,'t')
                 
                }
        motion = ''
        direction = grid[i][j]
        if direction == 4:
            return self.check(i,j+1,grid, 'r', valid, visited) or self.check(i+1,j,grid, 'd', valid, visited)
        if direction == 5:
            return False
        
        if direction == 1:
            j += 1
            motion = 'r'
        elif direction == 2:
            i += 1
            motion = 'd'
        elif direction == 3:
            i += 1
            motion = 'd'
        elif direction == 6:
            j += 1
            motion = 'r'
        
        
               
        
        return self.check(i,j,grid, motion, valid, visited)
        
        
        

                    

       
                
        