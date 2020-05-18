class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rests = {}
        min_sum = float('inf')
        answer = []
        for i, res in enumerate(list1):
            rests[res] = i
        # print(rests)
        for i, res in enumerate(list2):
            if res in rests.keys():
                sumVal = rests[res] + i
                if sumVal < min_sum:
                    answer = [res]
                    min_sum = sumVal
                elif sumVal == min_sum:
                    answer += [res]
        return answer
                