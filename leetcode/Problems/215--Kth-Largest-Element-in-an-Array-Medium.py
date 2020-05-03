import heapq
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        myHeap = []
        heapq.heapify(myHeap)
        for num in nums:
            # print(myHeap)
            if len(myHeap) >= k:
                top = heapq.heappop(myHeap)
                if num > top:
                    heapq.heappush(myHeap, num)
                else:
                    heapq.heappush(myHeap, top)
            else:
                heapq.heappush(myHeap, num)
        return heapq.heappop(myHeap)
            
        