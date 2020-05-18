class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.neighbours = {}
        for x,y in edges:
            if x in self.neighbours.keys():
                self.neighbours[x] += [y]
            else:
                self.neighbours[x] = [y]
        self.count = hasApple.count(True)
        if self.count == 0:
            return 0

       
        self.vertices = [False for _ in range(n)]    
        def dfs(vertex):
            val1, val2 = False, False
            if hasApple[vertex]:
                self.vertices[vertex] = True
                self.count -= 1
                if self.count == 0:
                    return True
                val1 = True
            if vertex not in self.neighbours.keys():
                return val1 or False
            for n in self.neighbours[vertex]:
                val = dfs(n)
                if val:
                    self.vertices[vertex] = True
                    val2 = True
            return val1 or val2
        dfs(0)
        
        return 2*self.vertices.count(True)-2
                
    
    
            