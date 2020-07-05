class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        answer = 0
        for num in left:
            answer = max(answer, num)
        for num in right:
            answer = max(answer, n-num)
        return answer