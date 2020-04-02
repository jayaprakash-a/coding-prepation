class Solution:
    def comparator(self, x):
        return x[0]**2 + x[1]**2
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        pointsSorted = sorted(points, key=self.comparator)
        
        return pointsSorted[:K]
        
# Better idea

# import heapq

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
#         heap = []
        
#         for (x, y) in points:
#             dist = -(x*x + y*y)
#             if len(heap) == K:
#                 heapq.heappushpop(heap, (dist, x, y))
#             else:
#                 heapq.heappush(heap, (dist, x, y))
        
#         return [(x,y) for (dist,x, y) in heap]