class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        def dfs(node, path):
            if node == len(graph)-1:
                answer.append(path + [node])
                return
            for adj in graph[node]:
                dfs(adj, path+[node])
        dfs(0, [])
        return answer
            