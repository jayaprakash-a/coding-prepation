class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         def floydWarshall(graph, n): 
#             # dist = map(lambda i : map(lambda j : j , i) , graph) 
#             for k in range(n): 
#                 for i in range(n): 
#                     for j in range(n): 
#                         graph[i][j] = min(graph[i][j] , graph[i][k]+ graph[k][j])
#             return graph
#         graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        
#         for [x, y] in connections:
#             graph[x][y] = 1
        
#         graph = floydWarshall(graph, n)
        # print('start') 
        answer = 0
        adj = [set() for _ in range(n)]
        nonadj = [set() for _ in range(n)]
        goodVertices = set()
        newSet = set()
                
                    
        goodVertices.add(0)
        for [x, y] in connections:
            adj[x].add(y)
            nonadj[y].add(x)
            if y == 0:
                goodVertices.add(x)
        
        for num in goodVertices:
            newSet |= nonadj[num]
        
        goodVertices |= newSet
        # print('beofre', goodVertices)
        
        while(len(goodVertices) != n):
            for num in goodVertices:
                newSet |= nonadj[num]

            goodVertices |= newSet
            # print(goodVertices)
            entries = list(goodVertices)
            for entry in entries:
                
                diff = adj[entry] - goodVertices
                # print(entry, diff)
                answer += len(diff)
                newSet = set()
                for num in diff:
                    newSet |= nonadj[num]
                diff |= newSet
                goodVertices |= diff
        
        return answer
        
        
        