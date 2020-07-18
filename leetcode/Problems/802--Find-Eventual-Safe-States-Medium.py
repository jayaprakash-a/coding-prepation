class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        out_degree = {}
        in_nodes = defaultdict(list)
        for node in range(len(graph)):
            out_degree[node] = len(graph[node])
            if out_degree[node] == 0:
                queue.append(node)
            for neigh in graph[node]:
                in_nodes[neigh].append(node)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for in_node in in_nodes[node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0:
                    queue.append(in_node)
        return sorted(result)