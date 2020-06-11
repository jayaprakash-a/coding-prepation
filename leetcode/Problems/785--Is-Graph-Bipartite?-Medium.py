class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        if len(graph) == 0:
            return True
        N = len(graph)
        color = [-1 for _ in range(N+1)]
        visited = [False for _ in range(N+1)]
        queue = collections.deque()
        someEntry = -1
        for entry in graph:
            for vertex in entry:
                someEntry = vertex
                break
            if someEntry != -1:
                break
        if someEntry == -1:
            return True
        queue.append(someEntry)
        color[someEntry] = 0
        
        for i in range(N):
            if not visited[i]:
                queue.append(i)
            while queue:
                entry = queue.popleft()
                visited[entry] = True
                # print(entry, len(graph))
                # print(graph[entry])
                for neighbour in graph[entry]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[entry]
                    if color[neighbour] == color[entry]:
                        return False
                    if not visited[neighbour]:
                        queue.append(neighbour)
        
        return True