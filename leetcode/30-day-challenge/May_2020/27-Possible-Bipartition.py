class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        adjList = [[] for _ in range(N+1)]
        color = [-1 for _ in range(N+1)]
        visited = [False for _ in range(N+1)]
        queue = collections.deque()
        for dislike in dislikes:
            adjList[dislike[0]] += [dislike[1]]
            adjList[dislike[1]] += [dislike[0]]
        
        queue.append(dislikes[0][0])
        color[dislikes[0][0]] = 0
        
        for i in range(1, N+1):
            if not visited[i]:
                queue.append(i)
            while queue:
                entry = queue.popleft()
                visited[entry] = True
                
                for neighbour in adjList[entry]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[entry]
                    if color[neighbour] == color[entry]:
                        return False
                    if not visited[neighbour]:
                        queue.append(neighbour)
        
        return True