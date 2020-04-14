class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for word in words:
            for other in words:
                if word in other and word != other:
                    answer.append(word)
                    break
        return answer
        