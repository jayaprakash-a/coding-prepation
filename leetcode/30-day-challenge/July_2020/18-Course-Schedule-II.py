class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i: set() for i in range(numCourses)}
        neigh = defaultdict(set)
        for [x, y] in prerequisites:
            edges[x].add(y)
            neigh[y].add(x)
        
        queue = deque()
        for i in range(numCourses):
            if len(edges[i]) == 0:
                queue.append(i)
        result = list(queue)

        while queue:
            node = queue.popleft()
            for adj in neigh[node]:
                edges[adj].remove(node)
                if len(edges[adj]) == 0:
                    queue.append(adj)
                    result.append(adj)
        return result if len(result) == numCourses else []
                
            