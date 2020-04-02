class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flatList = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flatList.append(grid[i][j])
        
        k = k%len(flatList)
        newList = [0]*len(flatList)
        
        for i in range(len(flatList)):
            newList[(i+k)%(len(flatList))] = flatList[i]
        
        index = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = newList[index]
                index += 1
        
        return grid
            