class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = [0 for _ in range(num_people)]
        current, index = 1, 0
        
        while candies:
            answer[index] += min(candies, current)
            candies -= min(candies, current)
            current += 1
            index += 1
            if index == num_people:
                index = 0
        return answer