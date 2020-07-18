class Solution:
    def minMutation(self, source: str, destination: str, words: List[str]) -> int:
        words.append(source)
        distance = [-1 for _ in range(len(words))]
        dist = collections.defaultdict(list)
        indices = {}
        for i in range(len(words)):
            indices[words[i]] = i
            for j in range(i+1, len(words)):
                diff = sum([1 for k in range(len(words[i])) if words[i][k] != words[j][k]])
                if diff == 1:
                    dist[words[i]].append(words[j])
                    dist[words[j]].append(words[i])
        distance[indices[source]] = 0
        queue = collections.deque()
        for word in dist[source]:
            distance[indices[word]] = 1
            queue.append(word)
        while queue:
            word = queue.popleft()
            if word == destination:
                return distance[indices[word]]
            for child in dist[word]:
                if distance[indices[child]] == -1:
                    distance[indices[child]] = distance[indices[word]]+1
                    queue.append(child)
        return -1