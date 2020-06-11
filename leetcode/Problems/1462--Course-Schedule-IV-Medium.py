class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        def floydWarshall(graph, n): 
            # dist = map(lambda i : map(lambda j : j , i) , graph) 
            for k in range(n): 
                for i in range(n): 
                    for j in range(n): 
                        graph[i][j] = min(graph[i][j] , graph[i][k]+ graph[k][j])
            return graph
        
        graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for [x, y] in prerequisites:
            graph[x][y] = 1
        dist = floydWarshall(graph, n)
        answer = []
        for [x, y] in queries:
            answer.append(dist[x][y] != float('inf'))
        
        return answer