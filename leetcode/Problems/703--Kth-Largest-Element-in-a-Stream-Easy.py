import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.myHeap = []
        heapq.heapify(self.myHeap)
        for num in nums:
            # print(myHeap)
            if len(self.myHeap) >= k:
                top = heapq.heappop(self.myHeap)
                if num > top:
                    heapq.heappush(self.myHeap, num)
                else:
                    heapq.heappush(self.myHeap, top)
            else:
                heapq.heappush(self.myHeap, num)
                

    def add(self, val: int) -> int:
        if len(self.myHeap) >= self.k:
            top = heapq.heappop(self.myHeap)
            if val > top:
                heapq.heappush(self.myHeap, val)
            else:
                heapq.heappush(self.myHeap, top)
        else:
            heapq.heappush(self.myHeap, val)
        # print(len(self.myHeap), self.myHeap)
        top = heapq.heappop(self.myHeap)
        heapq.heappush(self.myHeap, top)
        return top
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)