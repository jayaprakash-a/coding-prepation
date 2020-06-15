
class TreeAncestor:

    
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.child = [{} for _ in range(len(parent))]
        self.par = [{} for _ in range(len(parent))]
        for i in range(1, len(parent)):
            self.child[i][1] = parent[i]
            self.par[i][parent[i]] = 1
        # for i in range(n):
            # print(i, self.child[i], self.par[i])
        
        for i in range(len(parent)):
            count = 0
            p = collections.deque()
            for c in self.par[i]:
                p.append(c)
            # print(i, p)
            while p and count < 64:
                key = p.popleft()
                key = int(key)                
                for entry in self.par[key].keys():
                    entry = int(entry)
                    # print(i, entry, key, self.par[key], self.child[i])
                    if self.par[key][entry] + 1 not in self.child[i].keys():
                        self.child[i][self.par[key][entry] + 1] = entry
                        # print(i, entry, key, self.par[key], self.child[i])
                        self.par[i][entry] = self.par[key][entry] + 1
                        p.append(entry)
                        count += 1
                        if count == 64:
                            break
                        
            # print(i, self.child[i], self.par)
        # print(self.child)
    def getKthAncestor(self, node: int, k: int) -> int:       
        if k <= 0:
            return -1

        while True:
            # print(k, node, self.child[node])
            if k in self.child[node].keys():
                return self.child[node][k]
            maxLen = sorted(self.child[node].keys(), reverse=True)
            maxInd = 1
            for i in maxLen:
                if i < k:
                    maxInd = i
                    break
            if k <= 0 or maxInd not in self.child[node].keys():
                return -1
            # print('ind', maxInd)
            
            res = self.getKthAncestor(self.child[node][maxInd], k-maxInd)
            if res != -1:
                self.child[node][k] = res
                return self.child[node][k]
            return -1
            
            
        return -1


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)