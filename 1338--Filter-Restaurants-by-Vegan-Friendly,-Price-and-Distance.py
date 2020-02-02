class Solution:
    def comparator(self, x):
        return x[1], x[0]
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        vegFilter = []
        if veganFriendly == 0:
            vegFilter = restaurants
        else:
            vegFilter = list(filter(lambda x: x[2] == veganFriendly, restaurants) )
        
        
        priceFilter = list(filter(lambda x: x[3] <= maxPrice, vegFilter) )
        distFilter = list(filter(lambda x: x[4] <= maxDistance, priceFilter) )
        # print(distFilter)
        
    #     sortedOrder = x= [[8, 9, 7],
    # [1, 2, 3],
    # [5, 4, 3],
    # [4, 5, 6]]
        
        sortedList = sorted(distFilter, key = self.comparator, reverse=True)
        
        answer = list(map(lambda x: x[0], sortedList))
        
        
        return answer

        