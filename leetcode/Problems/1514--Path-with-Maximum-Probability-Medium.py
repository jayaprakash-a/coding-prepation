class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        prob = [0.0 for _ in range(n)]
        adjacent = defaultdict(set)
        # visited = {}
        def helper(x):
            return -x[1]
        for ([a,b],c) in zip(edges, succProb):
            adjacent[a].add((b, c))
            adjacent[b].add((a, c))
        # for entry in adjacent.keys():
        #     adjacent[entry] = sorted(adjacent[entry], key=helper)
        def bfs(node, value):
            queue = deque()
            for (adj, val) in adjacent[node]:
                queue.append((adj, prob[start]*val))
            while queue:
                (curr, value) = queue.popleft()
                prob[curr] = max(prob[curr], value)
                for (adj, val) in adjacent[curr]:
                    if prob[adj] < prob[curr]*val:
                        queue.append((adj, prob[curr]*val))
        prob[start] = 1.0
        bfs(start, 1.0)
        return prob[end]