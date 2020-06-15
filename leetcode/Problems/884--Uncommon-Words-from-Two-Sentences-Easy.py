class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:        
        cc = collections.Counter(A.split(' ')) +  collections.Counter(B.split(' '))              
        answer = [word for word in cc if cc[word] == 1]        
        return answer
                    