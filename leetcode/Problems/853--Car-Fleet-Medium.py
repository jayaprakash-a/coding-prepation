class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        
        
        carDetails = [[position[i], speed[i]] for i in range(len(position))]
        
        carDetails = sorted(carDetails, reverse=True)
        
        answer = 1
        time = (target - carDetails[0][0]) / carDetails[0][1]
        for i in range(1, len(carDetails)):
            val = (target - carDetails[i][0]) / carDetails[i][1]
            if val > time:
                answer += 1
                time = val
        return answer
        # print(carDetails)
        