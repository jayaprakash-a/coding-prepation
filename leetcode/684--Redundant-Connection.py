class Solution:
    def find_parent(self, parent, i): 
        # print(i, parent)
        if parent[i] == -1: 
            return i 
        if parent[i]!= -1: 
             return self.find_parent(parent,parent[i])
    
    def union(self,parent,x,y): 
        x_set = self.find_parent(parent, x) 
        y_set = self.find_parent(parent, y) 
        parent[x_set] = y_set 
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        answer = []
        parent = [-1]*(len(edges)) 
        for [i,j] in edges: 
            i, j = i-1, j-1
            x = self.find_parent(parent, i)  
            y = self.find_parent(parent, j) 
            if x == y: 
                answer = [i,j]
            else:
                self.union(parent,x,y) 
        
        return [answer[0]+1,answer[1]+1]
        