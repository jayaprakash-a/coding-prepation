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

obj = DisjointSet(5) 
obj.union(0, 2) 
obj.union(4, 2) 
obj.union(3, 1) 
if obj.find_parent(4) == obj.find_parent(0): 
    print('Yes') 
else: 
    print('No') 
if obj.find_parent(1) == obj.find_parent(0): 
    print('Yes') 
else: 
    print('No') 
