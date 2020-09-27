class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        products = {(0, 0): [grid[0][0], grid[0][0]]}
        
        dirs = [(0, 1), (1, 0)]
        
        
        queue = deque([(0, 0)])
        queueSet = set([(0, 0)])
        def valid(pos):
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                return True
            return False
       
        while queue:            
            pos = queue.popleft()
            # print(pos)
            queueSet.remove(pos)
            for dir in dirs:
                newpos = (pos[0]+dir[0], pos[1]+dir[1])
                # print(newpos, valid(newpos), len(grid), len(grid[0]))
                if valid(newpos):
                   
                    if newpos not in products:
                        products[newpos] = [max(grid[newpos[0]][newpos[1]]*products[pos][0], grid[newpos[0]][newpos[1]]*products[pos][1]), min(grid[newpos[0]][newpos[1]]*products[pos][0], grid[newpos[0]][newpos[1]]*products[pos][1])]
                        
                    else:
                        products[newpos][0] = max(products[newpos][0], grid[newpos[0]][newpos[1]]*products[pos][0], grid[newpos[0]][newpos[1]]*products[pos][1])
                        products[newpos][1] = min(products[newpos][1], grid[newpos[0]][newpos[1]]*products[pos][0], grid[newpos[0]][newpos[1]]*products[pos][1])
                    if newpos not in queueSet:
                        queue.append(newpos)
                        queueSet.add(newpos)
                
                
        end = (len(grid)-1, len(grid[0])-1)
        
        # print(products)
        # print('---------------')
        if products[end][0] < 0:
            return -1
        
        return products[end][0]%(10**9+7)
        
                    
            
        
        
        
        