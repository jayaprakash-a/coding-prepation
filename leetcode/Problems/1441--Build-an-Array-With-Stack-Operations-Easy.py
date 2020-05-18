class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer, i = [], 0
        curr = 1
        while i < len(target):
            if target[i] == curr:
                answer.append('Push')
                i += 1
            else:
                answer.append('Push')
                answer.append('Pop')
            curr += 1
        return answer
        