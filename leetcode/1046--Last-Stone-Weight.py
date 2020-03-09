import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = list(map(lambda x: -1*x, stones))
        
        heapq.heapify(stones)
        
        while(len(stones) != 1):
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            if val1 < val2:
                val1, val2 = val2, val1
            heapq.heappush(stones, val2-val1)
        
        # print(-1*stones[0])
        return -1*stones[0]
        