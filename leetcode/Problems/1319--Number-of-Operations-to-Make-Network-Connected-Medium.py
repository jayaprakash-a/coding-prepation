class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        if n > 1 + len(connections):
            return -1
        def find(i):
            if parent[i] == i:
                return parent[i]
            parent[i] = find(parent[i])            
            return parent[i]
        def union(i, j):
            parent[find(i)] = find(j)
        for x, y in connections:
            union(x, y)
        # print(parent)
        answer = sum([1 for i in range(n) if parent[i] == i])
        # for i in range(n):
        #     if parent[i] == i:
        #         answer += 1
        return answer - 1