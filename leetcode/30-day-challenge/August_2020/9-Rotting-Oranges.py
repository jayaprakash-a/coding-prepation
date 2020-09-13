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
        # print((0, 1) in fresh)
        # print(fresh)
        # print(rotten)
        # print('---------')
        while(len(fresh) > 0):
            # print(fresh)
            # print(rotten)
            # print('---------')
            newRotten = set()
            changed = False
            for (i, j) in rotten:
                for (x, y) in adj:
                    # print((i+x, j+y))
                    if (i+x, j+y) in fresh:
                        newRotten.add((i+x, j+y))
                        changed = True
            # print(changed)
            days += 1
            rotten = rotten.union(newRotten)
            fresh -= rotten
            if not changed:
                break
                
        if len(fresh) == 0:
            return days
        else:
            return -1
        