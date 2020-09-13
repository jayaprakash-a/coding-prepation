import collections
def getAns(parents, queries):
    children = collections.defaultdict(list)
    for i in range(len(parents)):
        children[parents[i]] += [i+2]
    values = [0 for _ in range(len(parents)+2)]
    def bfs():
        queue = collections.deque()
        for child in children[1]:
            queue.append(child)
        while queue:
            node = queue.popleft()
            values[node] = len(children[parents[node-2]])*values[parents[node-2]]
            for child in children[node]:
                if values[child] == 0:
                    queue.append(child)
    values[1] = 1
    bfs()
    for [a, b] in queries:
        if values[a] < values[b]:
            print(-1)
        elif values[a] == values[b]:
            print(0)
        else:
            print(1)
def main():
    [n, q] = list(map(int, input().split()))
    parents = []
    for _ in range(n-1):
        parents.append(int(input()))
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    getAns(parents, queries)
main()