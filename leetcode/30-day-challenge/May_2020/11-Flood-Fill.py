class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_colour = image[sr][sc]
        
        if len(image) == 0:
            return []
        if image[sr][sc] == newColor:
            return image
        m, n = len(image), len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def isValid(x, y):
            if x < m and x >= 0 and y >= 0 and y < n:
                return True
            return False
        def dfs(x, y):
            # print(x1, y1, x, y)
            visited[x][y] = True
            image[x][y] = newColor
            if isValid(x-1, y) and not visited[x-1][y] and image[x-1][y] == start_colour:
                dfs( x-1, y)
            if isValid(x+1, y) and not visited[x+1][y] and image[x+1][y] == start_colour:
                dfs(x+1, y)
            if isValid(x, y+1) and not visited[x][y+1] and image[x][y+1] == start_colour:
                dfs(x, y+1)
            if isValid(x, y-1) and not visited[x][y-1] and image[x][y-1] == start_colour:
                dfs(x, y-1)
        # if image[sr][sc] != newColor:
        dfs(sr, sc)
        return image