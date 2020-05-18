class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        return [candies[i]+extraCandies >= maxCandy for i in range(len(candies))]