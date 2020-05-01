class DisjointSet:
	def __init__(self, n):		
		self.parent = [i for i in range(n)]
		self.rank = [1 for i in range(n)]

	def find_parent(self, x):
		if self.parent[x] == x:
			return x
		if self.parent[x] != x:
			self.parent[x] = self.find_parent(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		xset = self.find_parent(x)
		yset = self.find_parent(y)
		if xset == yset:
			return
		if self.rank[xset] > self.rank[yset]:
			self.parent[yset] = xset
		elif self.rank[yset] > self.rank[xset]:
			self.parent[xset] = yset
		else:
			self.parent[yset] = xset
			self.rank[xset] += 1
            
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        union_find = DisjointSet(26)
        
        for expr in equations:
            if expr[1] == '=':
                union_find.union(ord(expr[0]) - ord('a'), ord(expr[3]) - ord('a'))
        
        for expr in equations:
            if expr[1] == '!':
                if union_find.find_parent(ord(expr[0]) - ord('a')) ==  union_find.find_parent(ord(expr[3]) - ord('a')):
                    return False
                                       

        return True