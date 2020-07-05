class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totalSum, sumVal = sum(distance), 0
        for i in range(min(start, destination), max(start, destination)):
            sumVal += distance[i]
        return min(sumVal, totalSum-sumVal)