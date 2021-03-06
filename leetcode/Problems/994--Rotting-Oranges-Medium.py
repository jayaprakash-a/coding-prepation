class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])        
        
        fresh, rotten = set(), set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        
        adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        days = 0

        while(len(fresh) > 0):

            newRotten = set()
            changed = False
            for (i, j) in rotten:
                for (x, y) in adj:
                    if (i+x, j+y) in fresh:
                        newRotten.add((i+x, j+y))
                        changed = True
            days += 1
            rotten = rotten.union(newRotten)
            fresh -= rotten
            if not changed:
                break
                
        if len(fresh) == 0:
            return days
        else:
            return -1
        