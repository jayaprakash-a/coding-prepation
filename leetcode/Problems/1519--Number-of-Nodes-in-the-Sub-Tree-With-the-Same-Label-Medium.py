class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0]*n
        children = defaultdict(list)
        childNode = set()
        parentNode = set()
        
        for [x, y] in edges:
            children[y].append(x)
            children[x].append(y)

        visited = set()

        def dfs(node):
            visited.add(node)
            string = labels[node]
            for child in children[node]:
                if child not in visited:
                    string += dfs(child)
            
            answer[node] = string.count(labels[node])
            
            return string
        dfs(0)
        
        return answer
            