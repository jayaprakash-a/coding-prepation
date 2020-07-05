class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        index = [0]*len(words)
        for i in range(len(S)):
            for j in range(len(words)):
                if len(words[j]) > index[j]:
                    if words[j][index[j]] == S[i]:
                        index[j] += 1
                    
        answer = 0
        for j in range(len(words)):
            if len(words[j]) == index[j]:
                answer += 1
        return answer
    
