class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        answer = []
        previous = 0
        for i in range(1, len(S)):
            # print(set(S[previous:i]).intersection(set(S[i:])))
            if len(set(S[previous:i]).intersection(set(S[i:]))) == 0:
                answer.append(i-previous)
                previous = i
        
        answer.append(len(S) - previous)
        return answer