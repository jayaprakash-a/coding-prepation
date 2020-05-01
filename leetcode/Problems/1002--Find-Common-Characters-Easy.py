class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        chars = collections.Counter(A[0])
        
        for i in range(1, len(A)):
#             & operator for counter returns the mininum
            chars &= collections.Counter(A[i])            
        
        return list(chars.elements())
        # answer = []
        # for ch in chars.keys():
        #     answer += [ch]*chars[ch]
        # return answer