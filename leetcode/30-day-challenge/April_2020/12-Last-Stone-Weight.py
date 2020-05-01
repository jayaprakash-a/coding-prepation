import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones) 
        while(len(stones) > 1):
            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)
            if x != y:
                stones.append(x-y)
                heapq._heapify_max(stones)
        
        if len(stones) == 0:
            return 0
        return stones[0]
            
             