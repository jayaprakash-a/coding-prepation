import sys
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst: 
            return 0
        maxVal = sys.maxsize
        d, seen = collections.defaultdict(list), collections.defaultdict(lambda: maxVal)
        
        for u, v, p in flights:
            d[u] += [(v, p)]
    
        q = collections.deque()
        q.append((src, -1, 0))
        
        while q:
            pos, k, cost = q.popleft()
            if pos == dst or k == K: continue 
            for neighbour, p in d[pos]:
                if cost + p >= seen[neighbour]:
                    continue
                else:
                    seen[neighbour] = cost+p
                    q.append((neighbour, k+1, cost+p))
        if seen[dst] < maxVal:
            return seen[dst]
        
        return -1