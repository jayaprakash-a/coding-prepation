class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        grid.insert(0, [0 for _ in range(n+2)])
        for i in range(1, n+1):
            grid[i].insert(0, 0)
            grid[i].append(0)
        grid.append([0 for _ in range(n+2)])
        # print(grid)
        answer = 0
        for i in range(1, n+2):
            for j in range(1, n+2):
                if grid[i][j] != 0:
                    count += 2
                answer += abs(grid[i][j] - grid[i][j-1])
                answer += abs(grid[i][j] - grid[i-1][j])
        return answer + count