class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        canDo = [0 for _ in range(numCourses)]
        
        for [x, y] in prerequisites:
            graph[x] += [y]
        
        def dfs(node):
            if canDo[node] == -1:
                return False
            elif canDo[node] == 1:
                return True
            canDo[node] = -1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            canDo[node] = 1
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True